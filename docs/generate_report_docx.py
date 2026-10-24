#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo file Báo cáo tổng hợp Microsoft Word (.docx) chuẩn quy định báo cáo thực tập / bài tập lớn
Môn học: Triển khai và Quản trị Hệ thống Phần mềm - Đề tài 3
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background(cell, fill_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def add_code_block(doc, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F4F6F8")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    # Custom border for code block (left border primary color)
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="0284C7"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph() # Spacing

def build_docx_report(output_path):
    doc = docx.Document()
    
    # Set page margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.0)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.paragraph_format.line_spacing = 1.3
    normal_style.paragraph_format.space_after = Pt(6)
    
    # =========================================================================
    # TRANG BÌA NGOÀI CÙNG (COVER PAGE)
    # =========================================================================
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(4)
    r = p1.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC CÔNG NGHỆ\nKHOA CÔNG NGHỆ THÔNG TIN")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(15, 23, 42)
    
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_div = p_div.add_run("-------------------- *** --------------------")
    r_div.bold = True
    r_div.font.color.rgb = RGBColor(100, 116, 139)
    
    doc.add_paragraph().paragraph_format.space_before = Pt(40)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("BÁO CÁO BÀI TẬP LỚN\n")
    r2.bold = True
    r2.font.size = Pt(20)
    r2.font.color.rgb = RGBColor(14, 116, 144)
    
    r2_sub = p2.add_run("MÔN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM\n\n")
    r2_sub.bold = True
    r2_sub.font.size = Pt(14)
    r2_sub.font.color.rgb = RGBColor(51, 65, 85)
    
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run("ĐỀ TÀI 3:\nWEBSITE QUẢNG BÁ SẢN PHẨM SỬ DỤNG WORDPRESS, REVERSE PROXY NGINX, PROMETHEUS, GRAFANA, LOKI VÀ BẢO MẬT GIA CỐ HỆ THỐNG (HARDENING)")
    r3.bold = True
    r3.font.size = Pt(14)
    r3.font.color.rgb = RGBColor(185, 28, 28)
    
    doc.add_paragraph().paragraph_format.space_before = Pt(60)
    
    # Table thông tin sinh viên
    table_info = doc.add_table(rows=6, cols=2)
    table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_info.autofit = False
    
    info_data = [
        ("Sinh viên thực hiện:", "Đặng Trần Hưng"),
        ("Mã số sinh viên (MSSV):", "20210001"),
        ("Lớp học phần:", "CNTT - K15"),
        ("Chuyên ngành:", "Kỹ thuật Phần mềm / An toàn Thông tin"),
        ("Giảng viên hướng dẫn:", "ThS. Nguyễn Văn B"),
        ("Năm học:", "Học kỳ I - Năm học 2026 - 2027")
    ]
    
    for i, (k, v) in enumerate(info_data):
        row = table_info.rows[i]
        c1, c2 = row.cells[0], row.cells[1]
        c1.width = Inches(2.6)
        c2.width = Inches(3.6)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c2, top=60, bottom=60, left=100, right=100)
        
        p_c1 = c1.paragraphs[0]
        p_c1.paragraph_format.space_before = Pt(0)
        p_c1.paragraph_format.space_after = Pt(0)
        r_k = p_c1.add_run(k)
        r_k.bold = True
        r_k.font.size = Pt(12)
        
        p_c2 = c2.paragraphs[0]
        p_c2.paragraph_format.space_before = Pt(0)
        p_c2.paragraph_format.space_after = Pt(0)
        r_v = p_c2.add_run(v)
        r_v.font.size = Pt(12)
        if i < 2:
            r_v.bold = True
            
    doc.add_paragraph().paragraph_format.space_before = Pt(60)
    
    p_bot = doc.add_paragraph()
    p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_bot = p_bot.add_run("Hà Nội, Tháng 10 Năm 2026")
    r_bot.italic = True
    r_bot.font.size = Pt(12)
    
    doc.add_page_break()
    
    # =========================================================================
    # LỜI CẢM ƠN & BẢNG NHẬN XÉT CỦA GIẢNG VIÊN
    # =========================================================================
    h_eval = doc.add_heading("BẢNG NHẬN XÉT CỦA GIẢNG VIÊN CHẤM ĐIỂM", level=1)
    h_eval.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    table_score = doc.add_table(rows=8, cols=4)
    table_score.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_score)
    
    headers = ["Tiêu chí đánh giá", "Điểm tối đa", "Điểm đạt được", "Ghi chú / Nhận xét"]
    widths = [Inches(3.2), Inches(1.0), Inches(1.1), Inches(1.5)]
    
    hdr_row = table_score.rows[0]
    for idx, name in enumerate(headers):
        cell = hdr_row.cells[idx]
        cell.width = widths[idx]
        set_cell_background(cell, "0284C7")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(name)
        run.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.size = Pt(10.5)
        
    score_data = [
        ("1. Quản lý mã nguồn & Git commit rõ ràng, README chuẩn", "1.5"),
        ("2. Triển khai Web WordPress & MySQL, phpMyAdmin", "2.0"),
        ("3. Cấu hình Nginx Reverse Proxy (HTTPS tự ký, Security Headers)", "1.5"),
        ("4. Tích hợp Giám sát Prometheus + Grafana Dashboards", "1.5"),
        ("5. Quản trị Log tập trung Loki + Promtail & Truy vấn LogQL", "1.5"),
        ("6. Kỹ thuật gia cố hệ thống Hardening (Non-root, Network Isolation)", "1.0"),
        ("7. Chất lượng Báo cáo tổng hợp >= 10 trang & Demo", "1.0"),
    ]
    
    for i, (crit, pts) in enumerate(score_data):
        row = table_score.rows[i+1]
        for c_idx, cell in enumerate(row.cells):
            cell.width = widths[c_idx]
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            if i % 2 == 1:
                set_cell_background(cell, "F8FAFC")
        row.cells[0].paragraphs[0].add_run(crit).font.size = Pt(10)
        p_pts = row.cells[1].paragraphs[0]
        p_pts.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_pts.add_run(pts).font.size = Pt(10)
        
    p_cmt = doc.add_paragraph()
    p_cmt.paragraph_format.space_before = Pt(20)
    p_cmt.add_run("Nhận xét chi tiết của Giảng viên:\n").bold = True
    p_cmt.add_run("..........................................................................................................................................................................\n"
                  "..........................................................................................................................................................................\n"
                  "..........................................................................................................................................................................\n")
    
    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.paragraph_format.space_before = Pt(30)
    r_sign = p_sign.add_run("Hà Nội, ngày ..... tháng ..... năm 2026\nGiảng viên chấm điểm\n(Ký và ghi rõ họ tên)")
    r_sign.italic = True
    
    doc.add_page_break()
    
    # =========================================================================
    # DANH MỤC THUẬT NGỮ VÀ CHỮ VIẾT TẮT
    # =========================================================================
    doc.add_heading("DANH MỤC CÁC CHỮ VIẾT TẮT", level=1)
    table_abbr = doc.add_table(rows=10, cols=3)
    table_abbr.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_abbr)
    
    abbr_hdr = table_abbr.rows[0]
    abbr_cols = ["Chữ viết tắt", "Cụm từ tiếng Anh nguyên gốc", "Ý nghĩa chuyên môn"]
    abbr_w = [Inches(1.5), Inches(2.3), Inches(2.8)]
    for idx, cname in enumerate(abbr_cols):
        cell = abbr_hdr.cells[idx]
        cell.width = abbr_w[idx]
        set_cell_background(cell, "0F766E")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(cname)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10.5)
        
    abbr_items = [
        ("API", "Application Programming Interface", "Giao diện lập trình ứng dụng"),
        ("CSP", "Content Security Policy", "Chính sách bảo mật nội dung trang web"),
        ("DBMS", "Database Management System", "Hệ quản trị cơ sở dữ liệu"),
        ("HSTS", "HTTP Strict Transport Security", "Cơ chế bắt buộc mã hóa HTTPS"),
        ("HTTPS", "Hypertext Transfer Protocol Secure", "Giao thức truyền tải web an toàn"),
        ("QPS", "Queries Per Second", "Số lượng truy vấn xử lý trên mỗi giây"),
        ("RPS", "Requests Per Second", "Số lượt yêu cầu web xử lý trên mỗi giây"),
        ("SAN", "Subject Alternative Name", "Mở rộng tên miền chứng chỉ SSL X.509"),
        ("XSS", "Cross-Site Scripting", "Lỗ hổng chèn mã độc kịch bản người dùng")
    ]
    for i, (a, b, c) in enumerate(abbr_items):
        row = table_abbr.rows[i+1]
        for c_idx, cell in enumerate(row.cells):
            cell.width = abbr_w[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if i % 2 == 1:
                set_cell_background(cell, "F0FDFA")
        r_a = row.cells[0].paragraphs[0].add_run(a)
        r_a.bold = True
        r_a.font.size = Pt(10)
        row.cells[1].paragraphs[0].add_run(b).font.size = Pt(10)
        row.cells[2].paragraphs[0].add_run(c).font.size = Pt(10)
        
    doc.add_page_break()
    
    # =========================================================================
    # NỘI DUNG CHÍNH CÁC CHƯƠNG (CHƯƠNG 1 -> CHƯƠNG 8)
    # =========================================================================
    
    # --- CHƯƠNG 1 ---
    doc.add_heading("CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI VÀ MỤC TIÊU TRIỂN KHAI", level=1)
    
    doc.add_heading("1.1. Bối cảnh và Tính cấp thiết của đề tài", level=2)
    doc.add_paragraph(
        "Trong bối cảnh chuyển đổi số và thương mại điện tử phát triển bùng nổ, các website quảng bá sản phẩm "
        "đóng vai trò sống còn trong việc tiếp cận khách hàng và xây dựng uy tín thương hiệu. Một hệ thống phần mềm "
        "khi đưa vào môi trường sản xuất (Production) không chỉ đòi hỏi tính năng phong phú mà còn phải đáp ứng nghiêm ngặt "
        "các tiêu chuẩn về tính sẵn sàng cao (High Availability), độ an toàn thông tin (Security), khả năng mở rộng linh hoạt "
        "(Scalability) và khả năng quan sát toàn diện (Observability)."
    )
    doc.add_paragraph(
        "Trước đây, các kiến trúc máy chủ nguyên khối (Monolithic bare-metal) cài đặt trực tiếp trên hệ điều hành bộc lộ "
        "rất nhiều yếu điểm: xung đột phiên bản thư viện phần mềm, khó khăn khi triển khai sao chép môi trường, thiếu cơ chế "
        "cô lập bảo mật khi bị tấn công và không có hệ thống thu thập số liệu hay nhật ký tập trung để cảnh báo sự cố. "
        "Đề tài này giải quyết toàn diện các thách thức trên bằng công nghệ Container hóa của Docker và Docker Compose, "
        "kết hợp lớp phòng thủ Nginx Reverse Proxy, hệ thống đo đạc Prometheus - Grafana, quản trị nhật ký Loki - Promtail "
        "và các biện pháp gia cố an ninh Hardening chuyên sâu."
    )
    
    doc.add_heading("1.2. Mục tiêu nghiên cứu và xây dựng hệ thống", level=2)
    doc.add_paragraph(
        "Dự án được triển khai nhằm đạt được các mục tiêu kỹ thuật cốt lõi sau:\n"
        "1. Đóng gói toàn bộ các dịch vụ bằng Docker Compose với các container biệt lập, dễ dàng khởi động chỉ bằng 1 câu lệnh.\n"
        "2. Triển khai website giới thiệu sản phẩm trên nền tảng WordPress 6.7, cơ sở dữ liệu MySQL 8.0 và công cụ quản trị phpMyAdmin.\n"
        "3. Xây dựng lớp bảo vệ biên giới bằng Nginx Reverse Proxy: tự động chuyển hướng HTTP 301 sang HTTPS, phát hành chứng chỉ SSL tự ký có Subject Alternative Name (SAN), cấu hình 7 tiêu đề an ninh HTTP (Security Headers) và giới hạn tốc độ truy cập (Rate Limiting).\n"
        "4. Phân tầng mạng cách ly (Network Isolation): Thiết lập 3 mạng riêng biệt (frontend, backend, monitoring), đảm bảo cổng cơ sở dữ liệu 3306 hoàn toàn không bị phơi nhiễm ra Internet.\n"
        "5. Giám sát toàn diện hiệu năng hệ thống: Thu thập chỉ số tài nguyên container (cAdvisor), lưu lượng máy chủ web (Nginx Exporter) và hiệu năng truy vấn cơ sở dữ liệu (MySQL Exporter), hiển thị qua các bảng điều khiển Grafana được khởi tạo tự động.\n"
        "6. Thu thập và phân tích nhật ký tập trung với Grafana Loki và Promtail: Xây dựng bộ 5 câu truy vấn LogQL chuyên sâu nhằm điều tra sự cố và phát hiện tấn công trong thời gian thực.\n"
        "7. Thực hiện gia cố an ninh (Hardening): Chạy container dưới người dùng non-root, áp dụng nguyên tắc đặc quyền tối thiểu (Least Privilege), quản lý biến môi trường an toàn và vô hiệu hóa các vector tấn công WordPress nguy hiểm."
    )
    
    doc.add_heading("1.3. Ngăn xếp công nghệ sử dụng (Technology Stack)", level=2)
    table_tech = doc.add_table(rows=7, cols=3)
    table_tech.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_tech)
    
    t_hdr = table_tech.rows[0]
    t_titles = ["Thành phần hệ thống", "Công nghệ & Phiên bản", "Vai trò và Nhiệm vụ đảm nhiệm"]
    t_w = [Inches(1.8), Inches(2.2), Inches(2.6)]
    for idx, cname in enumerate(t_titles):
        cell = t_hdr.cells[idx]
        cell.width = t_w[idx]
        set_cell_background(cell, "0284C7")
        set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(cname)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10)
        
    tech_data = [
        ("Reverse Proxy & SSL", "Nginx 1.27 (Alpine)", "Điểm tiếp nhận lưu lượng duy nhất, SSL Termination, Security Headers, Rate Limiting"),
        ("Ứng dụng Web", "WordPress 6.7 (Apache)", "Website quảng bá sản phẩm, quản lý bài viết và hình ảnh"),
        ("Cơ sở dữ liệu", "MySQL 8.0 & phpMyAdmin", "Lưu trữ dữ liệu quan hệ tối ưu hóa hiệu năng và giao diện web quản trị DB"),
        ("Hệ thống Giám sát", "Prometheus 2.50 + Grafana 10.4", "Thu thập chuỗi số liệu thời gian thực và trực quan hóa qua biểu đồ Dashboard"),
        ("Bộ xuất chỉ số (Exporters)", "cAdvisor 0.49, MySQL & Nginx Exp.", "Thu thập tài nguyên CPU/RAM container, QPS MySQL và RPS Nginx"),
        ("Hệ thống Nhật ký", "Loki 2.9 + Promtail 2.9", "Thu thập access/error log tập trung và hỗ trợ truy vấn LogQL"),
    ]
    for i, (a, b, c) in enumerate(tech_data):
        row = table_tech.rows[i+1]
        for c_idx, cell in enumerate(row.cells):
            cell.width = t_w[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if i % 2 == 1:
                set_cell_background(cell, "F8FAFC")
        row.cells[0].paragraphs[0].add_run(a).bold = True
        row.cells[1].paragraphs[0].add_run(b)
        row.cells[2].paragraphs[0].add_run(c)
        
    doc.add_page_break()
    
    # --- CHƯƠNG 2 ---
    doc.add_heading("CHƯƠNG 2: THIẾT KẾ KIẾN TRÚC HỆ THỐNG VÀ PHÂN TẦNG MẠNG", level=1)
    
    doc.add_heading("2.1. Kiến trúc tổng thể hệ thống (High-Level Architecture)", level=2)
    doc.add_paragraph(
        "Hệ thống được thiết kế theo mô hình kiến trúc phân tầng dạng Micro-services. Toàn bộ lưu lượng từ bên ngoài "
        "đều bị chặn tại biên giới và bắt buộc phải đi qua Nginx Reverse Proxy. Nginx đảm nhiệm việc giải mã SSL (SSL Termination), "
        "kiểm tra các tiêu chuẩn bảo mật, giới hạn tần suất yêu cầu và chuyển tiếp gói tin tới các dịch vụ phù hợp trong mạng nội bộ."
    )
    
    arch_diagram = (
        "+-----------------------------------------------------------------------------------------+\n"
        "|                            CLIENT / INTERNET BROWSER                                    |\n"
        "+--------------------------------------------+--------------------------------------------+\n"
        "                                             | (Port 80 HTTP -> 301 Redirect HTTPS)\n"
        "                                             | (Port 443 HTTPS - SSL / TLS 1.3)\n"
        "                                             v\n"
        "+-----------------------------------------------------------------------------------------+\n"
        "|                               NGINX REVERSE PROXY                                       |\n"
        "|                 (SSL Termination, Security Headers, Rate Limiting)                      |\n"
        "+-------------------+------------------------+--------------------------------------------+\n"
        "                    | (frontend-net)         | (frontend-net)                             |\n"
        "                    v                        v                                            |\n"
        "+-----------------------+  +------------------------+  +-------------------------------+  |\n"
        "|   WordPress 6.7 App   |  |   phpMyAdmin 5.2 GUI   |  |     Grafana 10.4 Dashboard    |  |\n"
        "|       (Cổng 80)       |  |       (Cổng 80)        |  |          (Cổng 3000)          |  |\n"
        "+-----------+-----------+  +------------+-----------+  +---------------+---------------+  |\n"
        "            | (backend-net)             | (backend-net)                |                  |\n"
        "            +-------------+-------------+                              |                  |\n"
        "                          v                                            |                  |\n"
        "+---------------------------------------------------+                  |                  |\n"
        "|                  MySQL 8.0 SERVER                 |                  |                  |\n"
        "|      (Port 3306 KHÔNG mở ra ngoài máy chủ Host)   |                  |                  |\n"
        "+-------------------------+-------------------------+                  |                  |\n"
        "                          ^                                            |                  |\n"
        "                          | (backend-net)                              |                  |\n"
        "+-------------------------+-------------------------+                  |                  |\n"
        "|      MySQL Exporter (Thu thập chỉ số QPS, Uptime) |                  |                  |\n"
        "+-------------------------+-------------------------+                  |                  |\n"
        "                          |                                            |                  |\n"
        "                          | (monitoring-net)                           |                  |\n"
        "                          v                                            v                  |\n"
        "+-----------------------------------------------------------------------------------------+\n"
        "|                         OBSERVABILITY & LOGGING INFRASTRUCTURE                          |\n"
        "|  [Prometheus Metrics] <--- (cAdvisor Container Stats, Nginx Exporter, MySQL Exporter)   |\n"
        "|  [Loki Centralized Log] <--- (Promtail Agent scrapes Nginx access.log and error.log)    |\n"
        "+-----------------------------------------------------------------------------------------+\n"
    )
    add_code_block(doc, arch_diagram)
    
    doc.add_heading("2.2. Phân tầng mạng cách ly (Network Isolation Design)", level=2)
    doc.add_paragraph(
        "Nhằm tuân thủ nguyên tắc phòng thủ đa lớp (Defense in Depth) và mô hình không tin cậy (Zero Trust), "
        "hệ thống tạo ra 3 mạng bridge độc lập trong Docker Compose:\n"
        "1. net_production_frontend: Kết nối Nginx với WordPress, phpMyAdmin và Grafana. Người dùng bên ngoài chỉ truy cập được các dịch vụ này qua cổng 443 của Nginx.\n"
        "2. net_production_backend: Kết nối nội bộ giữa WordPress, phpMyAdmin, MySQL và MySQL Exporter. Máy chủ MySQL tuyệt đối không kết nối với mạng frontend và không ánh xạ cổng ra ngoài host. Kẻ tấn công quét cổng máy chủ vật lý sẽ hoàn toàn không phát hiện cổng 3306.\n"
        "3. net_production_monitoring: Kết nối độc lập dành cho Prometheus, Grafana, Loki, Promtail và các Exporter, đảm bảo dữ liệu giám sát không cạnh tranh băng thông với luồng truy cập của khách hàng."
    )
    
    doc.add_heading("2.3. Thiết kế lưu trữ dữ liệu bền vững (Volume Persistence)", level=2)
    doc.add_paragraph(
        "Mọi dữ liệu cốt lõi đều được bảo vệ an toàn thông qua các Docker Named Volumes, đảm bảo không bị mất mát dữ liệu "
        "khi cập nhật hoặc nâng cấp container:\n"
        "- vol_production_mysql_data: Lưu trữ tệp dữ liệu bảng, chỉ mục và transaction logs của MySQL 8.0.\n"
        "- vol_production_wordpress_data: Lưu trữ mã nguồn, các tệp media và ảnh sản phẩm do người dùng tải lên.\n"
        "- vol_production_nginx_logs: Volume chia sẻ giữa Nginx và Promtail để Promtail liên tục theo dõi tệp log.\n"
        "- vol_production_prometheus_data: Lưu trữ cơ sở dữ liệu chuỗi thời gian (TSDB) trong 15 ngày.\n"
        "- vol_production_grafana_data: Lưu trữ tài khoản người dùng, cấu hình giao diện Grafana.\n"
        "- vol_production_loki_data: Lưu trữ các khối log nén của Loki."
    )
    
    doc.add_page_break()
    
    # --- CHƯƠNG 3 ---
    doc.add_heading("CHƯƠNG 3: HIỆN THỰC ỨNG DỤNG WEB & NGINX REVERSE PROXY (COMMIT 1)", level=1)
    doc.add_paragraph(
        "Giai đoạn đầu tiên (tương ứng Commit 1) tập trung xây dựng nền móng ứng dụng và lớp bảo mật biên giới Nginx."
    )
    
    doc.add_heading("3.1. Triển khai dịch vụ WordPress Showcase", level=2)
    doc.add_paragraph(
        "Ứng dụng web giới thiệu sản phẩm sử dụng hình ảnh chính thức wordpress:6.7-apache. "
        "Để hoạt động trơn tru phía sau Reverse Proxy Nginx, biến môi trường WORDPRESS_CONFIG_EXTRA được đưa vào cấu hình:\n"
        "Khi Nginx gửi tiêu đề HTTP_X_FORWARDED_PROTO: https, WordPress nhận diện và thiết lập cờ $_SERVER['HTTPS'] = 'on'. "
        "Cấu hình này bắt buộc toàn bộ URL của bài viết, hình ảnh và tệp Javascript tải về máy khách phải sử dụng tiền tố https://, "
        "loại bỏ triệt để lỗi Mixed Content thường gặp khiến trang web bị vỡ giao diện."
    )
    
    doc.add_heading("3.2. Cấu hình Cơ sở dữ liệu MySQL 8.0 & phpMyAdmin", level=2)
    doc.add_paragraph(
        "MySQL 8.0 được cấu hình với các tham số tối ưu hiệu năng và an toàn cao trong mysql/conf.d/my.cnf:\n"
        "- innodb_buffer_pool_size = 256M: Tối ưu bộ nhớ đệm cho dữ liệu danh mục sản phẩm.\n"
        "- max_connections = 150: Giới hạn số lượng kết nối tối đa phòng chống cạn kiệt tài nguyên.\n"
        "- local_infile = 0: Vô hiệu hóa nạp tệp từ client, triệt tiêu lỗ hổng đọc file tùy ý trên máy chủ.\n"
        "- skip_symbolic_links = 1: Vô hiệu hóa liên kết mềm để ngăn tấn công duyệt thư mục.\n"
        "Đồng thời, phpMyAdmin được cấu hình tham số PMA_ABSOLUTE_URI: https://localhost/pma/ giúp hoạt động hoàn hảo "
        "dưới tiền tố đường dẫn /pma/ được Nginx định tuyến."
    )
    
    doc.add_heading("3.3. Cấu hình Nginx Reverse Proxy & Chuyển hướng HTTPS", level=2)
    doc.add_paragraph(
        "Nginx được cấu hình với 2 khối máy chủ (Server Blocks) trong nginx/conf.d/default.conf:\n"
        "1. Khối Server cổng 80: Tiếp nhận mọi yêu cầu HTTP và chuyển hướng vĩnh viễn (HTTP 301) sang cổng 443: return 301 https://$host$request_uri;\n"
        "2. Khối Server cổng 443: Tiếp nhận lưu lượng HTTPS, kích hoạt giao thức HTTP/2, áp dụng bộ mã hóa hiện đại TLSv1.2 và TLSv1.3, vô hiệu hóa các thuật toán mã hóa yếu."
    )
    
    doc.add_heading("3.4. Khởi tạo Chứng chỉ SSL tự ký với SAN (Subject Alternative Name)", level=2)
    doc.add_paragraph(
        "Để đáp ứng các tiêu chuẩn khắt khe của trình duyệt hiện đại (như Chrome, Edge), chứng chỉ SSL tự ký được khởi tạo "
        "thông qua script tự động hóa với phần mở rộng Subject Alternative Name (SAN), hỗ trợ đồng thời các tên miền "
        "localhost, *.localhost, wp.local, pma.local và địa chỉ IP 127.0.0.1, ::1."
    )
    
    doc.add_heading("3.5. Triển khai các Security Headers bảo vệ", level=2)
    doc.add_paragraph(
        "Tệp cấu hình nginx/security-headers.conf bổ sung toàn diện 7 tiêu đề an ninh theo khuyến cáo của tổ chức OWASP:\n"
        "- X-Frame-Options: SAMEORIGIN - Ngăn chặn tấn công Clickjacking.\n"
        "- X-Content-Type-Options: nosniff - Ngăn chặn MIME-sniffing.\n"
        "- X-XSS-Protection: 1; mode=block - Kích hoạt bộ lọc chống XSS.\n"
        "- Strict-Transport-Security: max-age=31536000; includeSubDomains; preload - Bắt buộc HTTPS trong 1 năm.\n"
        "- Referrer-Policy: strict-origin-when-cross-origin - Bảo vệ tính riêng tư của URL giới thiệu.\n"
        "- Content-Security-Policy: Giới hạn nguồn tài nguyên nạp vào trình duyệt.\n"
        "- Permissions-Policy: Vô hiệu hóa camera, microphone và định vị vị trí."
    )
    
    doc.add_heading("3.6. Cơ chế giới hạn tốc độ (Rate Limiting) & Chặn truy cập nhạy cảm", level=2)
    doc.add_paragraph(
        "Nginx thiết lập hai vùng kiểm soát tốc độ (Rate Limiting):\n"
        "- general_limit: Giới hạn tối đa 20 request/giây cho toàn trang web, hấp thụ lưu lượng bùng nổ lên tới 30 requests.\n"
        "- login_limit: Giới hạn tối đa 3 request/giây cho đường dẫn /wp-login.php, triệt tiêu hoàn toàn các đợt tấn công dò mật khẩu tự động.\n"
        "Đồng thời, Nginx chặn tuyệt đối endpoint /xmlrpc.php, chặn thực thi mã PHP trong thư mục tải lên wp-content/uploads, "
        "và chặn truy cập toàn bộ các tệp cấu hình ẩn như .env, .git, .htaccess."
    )
    
    doc.add_page_break()
    
    # --- CHƯƠNG 4 ---
    doc.add_heading("CHƯƠNG 4: HỆ THỐNG GIÁM SÁT TOÀN DIỆN VỚI PROMETHEUS & GRAFANA (COMMIT 2)", level=1)
    doc.add_paragraph(
        "Giai đoạn hai (tương ứng Commit 2) xây dựng hạ tầng quan sát (Observability) giúp quản trị viên nắm bắt "
        "tình trạng sức khỏe của toàn bộ hệ thống theo thời gian thực."
    )
    
    doc.add_heading("4.1. Kiến trúc hệ thống giám sát khả năng quan sát", level=2)
    doc.add_paragraph(
        "Hệ thống giám sát bao gồm 3 tầng thành phần chính:\n"
        "- Tầng đo đạc (Exporters): Đọc số liệu nội bộ từ hệ điều hành và các ứng dụng, chuyển đổi thành định dạng số liệu chuẩn Prometheus.\n"
        "- Tầng lưu trữ (Prometheus TSDB): Định kỳ kéo (Pull/Scrape) dữ liệu từ các exporter theo chu kỳ cấu hình (10s - 15s) và lưu trữ cục bộ.\n"
        "- Tầng hiển thị (Grafana Visual): Kết nối vào Prometheus để hiển thị các đồ thị trực quan và hỗ trợ cảnh báo ngưỡng."
    )
    
    doc.add_heading("4.2. Cấu hình Prometheus Server & Chiến lược Scrape Targets", level=2)
    doc.add_paragraph(
        "Tệp cấu hình monitoring/prometheus/prometheus.yml khai báo 5 Scrape Jobs độc lập:\n"
        "1. prometheus: Tự giám sát tình trạng bộ nhớ và hiệu năng của chính Prometheus.\n"
        "2. cadvisor: Giám sát toàn bộ container trên cổng 8080 với chu kỳ 10 giây.\n"
        "3. nginx: Giám sát lưu lượng máy chủ Nginx qua cổng 9113 của Nginx Exporter.\n"
        "4. mysql: Giám sát cơ sở dữ liệu qua cổng 9104 của MySQL Exporter.\n"
        "5. node-exporter: Giám sát tài nguyên CPU, RAM, ổ cứng của máy chủ host trên cổng 9100."
    )
    
    doc.add_heading("4.3. Giám sát Container với cAdvisor", level=2)
    doc.add_paragraph(
        "cAdvisor cung cấp các chỉ số chi tiết về mức tiêu thụ tài nguyên của từng container:\n"
        "- Tỷ lệ CPU tiêu thụ: sum(rate(container_cpu_usage_seconds_total[1m])) by (name) * 100\n"
        "- Dung lượng bộ nhớ RAM chiếm dụng: sum(container_memory_usage_bytes) by (name)\n"
        "- Tốc độ truyền tải mạng vào/ra (RX/TX Throughput): sum(rate(container_network_receive_bytes_total[1m]))"
    )
    
    doc.add_heading("4.4. Giám sát Database với MySQL Exporter", level=2)
    doc.add_paragraph(
        "MySQL Exporter kết nối an toàn với quyền tối thiểu, cung cấp các chỉ số quan trọng:\n"
        "- Thời gian máy chủ DB hoạt động liên tục: mysql_global_status_uptime\n"
        "- Tốc độ truy vấn SQL trên mỗi giây (QPS): rate(mysql_global_status_queries[1m])\n"
        "- Số lượng kết nối đang hoạt động: mysql_global_status_threads_connected\n"
        "- Băng thông mạng dữ liệu vào/ra: bytes_received và bytes_sent."
    )
    
    doc.add_heading("4.5. Giám sát Web Server với Nginx Prometheus Exporter", level=2)
    doc.add_paragraph(
        "Nginx Exporter đọc số liệu từ endpoint nội bộ http://nginx:8080/stub_status:\n"
        "- Tốc độ yêu cầu HTTP trên mỗi giây (RPS): rate(nginx_http_requests_total[1m])\n"
        "- Tổng số kết nối client đang mở (Active Connections): nginx_connections_active\n"
        "- Phân bố trạng thái kết nối: Reading (đang đọc request), Writing (đang gửi phản hồi), Waiting (đang nhàn rỗi trong chế độ Keep-Alive)."
    )
    
    doc.add_heading("4.6. Tự động khởi tạo Dashboards & Datasources trên Grafana", level=2)
    doc.add_paragraph(
        "Thông qua cơ chế Provisioning tự động, khi khởi động container production-grafana:\n"
        "- Tự động kết nối nguồn dữ liệu Prometheus tại http://prometheus:9090.\n"
        "- Tự động nạp sẵn 3 Dashboards chuyên nghiệp từ các tệp JSON:\n"
        "  + docker-containers.json: Bảng điều khiển tài nguyên toàn bộ container.\n"
        "  + nginx-overview.json: Bảng điều khiển lưu lượng mạng và số kết nối Nginx.\n"
        "  + mysql-overview.json: Bảng điều khiển QPS, kết nối và băng thông MySQL."
    )
    
    doc.add_page_break()
    
    # --- CHƯƠNG 5 ---
    doc.add_heading("CHƯƠNG 5: HỆ THỐNG GHI LOG TẬP TRUNG LOKI & PROMTAIL (COMMIT 3)", level=1)
    doc.add_paragraph(
        "Giai đoạn ba (tương ứng Commit 3) triển khai giải pháp quản trị nhật ký tập trung nhằm giúp đội ngũ "
        "vận hành nhanh chóng tìm kiếm nguyên nhân gốc rễ (Root Cause Analysis) và phát hiện các sự cố bất thường."
    )
    
    doc.add_heading("5.1. Thách thức trong quản lý Log và Giải pháp Grafana Loki", level=2)
    doc.add_paragraph(
        "Trong kiến trúc micro-services, nhật ký nằm rải rác bên trong từng container và dễ bị xóa mất khi container khởi động lại. "
        "Grafana Loki là giải pháp hiện đại được thiết kế theo tư duy của Prometheus: Loki không đánh chỉ mục toàn văn bản (tiết kiệm 80% bộ nhớ "
        "so với Elasticsearch), mà chỉ đánh chỉ mục cho các nhãn siêu dữ liệu (Labels) và nén nội dung log thành các khối dữ liệu Chunks. "
        "Nhờ đó, hệ thống vận hành cực kỳ nhẹ nhàng nhưng vẫn đảm bảo tốc độ tìm kiếm tức thì."
    )
    
    doc.add_heading("5.2. Cấu hình Promtail Agent thu thập nhật ký", level=2)
    doc.add_paragraph(
        "Promtail hoạt động như một agent thu thập nhật ký ngầm:\n"
        "- Promtail chia sẻ volume nginx_logs:/var/log/nginx:ro từ Nginx.\n"
        "- Tệp logging/promtail/promtail-config.yaml cấu hình job nginx theo dõi liên tục access.log và error.log.\n"
        "- Promtail tự động gắn các nhãn siêu dữ liệu {job=\"nginx\", env=\"production\", service=\"reverse-proxy\"} và đẩy dữ liệu về Loki qua cổng 3100."
    )
    
    doc.add_heading("5.3. Ngôn ngữ truy vấn LogQL và phân tích cú pháp", level=2)
    doc.add_paragraph(
        "LogQL cung cấp cú pháp trực quan gồm hai phần: Bộ chọn luồng nhật ký (Stream Selector) ví dụ {job=\"nginx\"} "
        "kết hợp với bộ lọc dòng nhật ký (Filter Expressions) như |= (chứa chuỗi), != (không chứa), |~ (khớp regex). "
        "Ngoài ra, LogQL cho phép chuyển đổi dòng nhật ký thành đồ thị đo lường (Metric Queries) qua các hàm count_over_time và rate."
    )
    
    doc.add_heading("5.4. Hiện thực 5 câu truy vấn LogQL thực tế theo đề bài", level=2)
    doc.add_paragraph("Dự án xây dựng và chuẩn hóa 5 câu truy vấn LogQL phục vụ kiểm thử và giám sát thực tế:")
    
    queries = [
        ("Query 1: Truy xuất toàn bộ log của Nginx Reverse Proxy",
         '{job="nginx"}',
         "Hiển thị toàn bộ dòng nhật ký truy cập và sự kiện lỗi thời gian thực được thu thập từ Nginx."),
        ("Query 2: Lọc các yêu cầu HTTP gặp lỗi phía Khách hàng (4xx) hoặc Máy chủ (5xx)",
         '{job="nginx"} |~ " (4\\\\d{2}|5\\\\d{2}) "',
         "Phát hiện các lỗi truy cập trang web như 403 Forbidden, 404 Not Found, 500 Server Error và 502 Bad Gateway."),
        ("Query 3: Giám sát nỗ lực dò quét nhạy cảm và tấn công XML-RPC (Security Alerts)",
         '{job="nginx"} |= "403" or {job="nginx"} |= "xmlrpc.php"',
         "Lọc nhanh các sự kiện bị Nginx từ chối truy cập và các nỗ lực tấn công brute force vào WordPress."),
        ("Query 4: Tính toán tốc độ phát sinh lỗi HTTP theo thời gian (Metric Query)",
         'sum(rate({job="nginx"} |~ " (4\\\\d{2}|5\\\\d{2}) " [5m]))',
         "Biến đổi dòng log thành đồ thị chỉ số trên Grafana đo tốc độ phát sinh lỗi trên mỗi giây trong cửa sổ 5 phút."),
        ("Query 5: Lọc các thông điệp cảnh báo và lỗi nghiêm trọng trong error.log",
         '{job="nginx", filename=~".*error.log"} |= "error" or {job="nginx", filename=~".*error.log"} |= "warn"',
         "Hỗ trợ quản trị viên điều tra lỗi bắt tay SSL, lỗi cấu hình hoặc mất kết nối mạng nội bộ giữa Nginx và upstream.")
    ]
    
    for title, q_code, q_desc in queries:
        doc.add_paragraph(title).bold = True
        add_code_block(doc, q_code)
        doc.add_paragraph(f"Giải thích ý nghĩa: {q_desc}")
        
    doc.add_page_break()
    
    # --- CHƯƠNG 6 ---
    doc.add_heading("CHƯƠNG 6: CÁC BIỆN PHÁP GIA CỐ VÀ BẢO MẬT HỆ THỐNG (HARDENING)", level=1)
    doc.add_paragraph(
        "Gia cố hệ thống (Hardening) là tiêu chuẩn bắt buộc để đảm bảo an toàn cho môi trường sản xuất thực tế. "
        "Dự án đã áp dụng toàn diện 6 nhóm biện pháp kỹ thuật:"
    )
    
    doc.add_heading("6.1. Vận hành Non-Root Containers", level=2)
    doc.add_paragraph(
        "Chạy container dưới quyền root tiềm ẩn nguy cơ kẻ tấn công thoát khỏi container (Container Escape) "
        "khi khai thác được lỗ hổng RCE. Dự án cấu hình:\n"
        "- Prometheus vận hành dưới người dùng không đặc quyền user: \"nobody\" (UID 65534).\n"
        "- Loki vận hành dưới người dùng riêng biệt user: \"10001:10001\".\n"
        "- Toàn bộ các tệp cấu hình (Nginx conf, SSL certs, MySQL conf, Prometheus yml, Promtail yml) "
        "đều được mount vào container dưới quyền chỉ đọc (:ro - Read-Only), ngăn chặn mã độc chỉnh sửa file cấu hình."
    )
    
    doc.add_heading("6.2. Network Isolation & Bảo vệ Cổng Database", level=2)
    doc.add_paragraph(
        "Áp dụng nguyên tắc cô lập phân tầng mạng:\n"
        "- Cơ sở dữ liệu MySQL 8.0 chỉ lắng nghe trên mạng nội bộ net_production_backend.\n"
        "- Cổng 3306 tuyệt đối không được ánh xạ (ports binding) ra máy chủ host.\n"
        "- Nginx Reverse Proxy và người dùng Internet hoàn toàn không thể chạm tới giao diện mạng của MySQL, "
        "loại bỏ triệt để nguy cơ tấn công brute force mật khẩu cơ sở dữ liệu từ bên ngoài."
    )
    
    doc.add_heading("6.3. Nguyên tắc đặc quyền tối thiểu (Least Privilege)", level=2)
    doc.add_paragraph(
        "Mỗi thành phần trong hệ thống chỉ được cấp đúng và đủ quyền hạn cần thiết để vận hành:\n"
        "- Ứng dụng WordPress chỉ được cấp tài khoản wp_user giới hạn phạm vi trên cơ sở dữ liệu wordpress_db.\n"
        "- Bộ xuất chỉ số MySQL Exporter sử dụng tài khoản chuyên dụng exporter, chỉ sở hữu quyền đọc thống kê hệ thống "
        "(PROCESS, REPLICATION CLIENT, SELECT), hoàn toàn bị cấm các lệnh INSERT, UPDATE, DELETE, DROP và giới hạn tối đa 5 kết nối."
    )
    
    doc.add_heading("6.4. Quản lý bí mật an toàn với .env", level=2)
    doc.add_paragraph(
        "Tuyệt đối không lưu trữ thông tin mật khẩu hoặc khóa bí mật bên trong mã nguồn hay tệp cấu hình git:\n"
        "- Toàn bộ mật khẩu root MySQL, mật khẩu database, mật khẩu Grafana admin đều được quản lý tập trung trong tệp .env.\n"
        "- Tệp .env được đưa vào danh sách loại trừ trong .gitignore, ngăn ngừa rò rỉ thông tin lên GitHub công khai.\n"
        "- Cung cấp tệp mẫu .env.example để hỗ trợ triển khai chuẩn hóa."
    )
    
    doc.add_heading("6.5. Gia cố bảo mật Nginx và triệt tiêu lỗ hổng WordPress", level=2)
    doc.add_paragraph(
        "Máy chủ web Nginx được thiết lập như một tường lửa ứng dụng web cơ bản:\n"
        "- server_tokens off;: Ẩn thông tin phiên bản Nginx, tránh bị dò quét lỗ hổng theo CVE.\n"
        "- Chặn đứng tấn công XML-RPC qua endpoint /xmlrpc.php.\n"
        "- Chặn đứng việc thực thi tệp kịch bản PHP trong thư mục tải lên wp-content/uploads/.\n"
        "- Chặn toàn bộ các tệp cấu hình và tệp ẩn (.env, .git, .htaccess).\n"
        "- Áp dụng đầy đủ 7 tiêu đề an ninh HTTP (Security Headers) chuẩn OWASP."
    )
    
    doc.add_page_break()
    
    # --- CHƯƠNG 7 ---
    doc.add_heading("CHƯƠNG 7: KỊCH BẢN KIỂM THỬ, ĐÁNH GIÁ VÀ HƯỚNG DẪN VẬN HÀNH", level=1)
    doc.add_paragraph(
        "Hệ thống cung cấp kịch bản kiểm thử tự động hóa thông qua hai script scripts/test-system.ps1 (PowerShell) "
        "và scripts/test-system.sh (Linux/Bash), thực hiện kiểm tra 4 kịch bản nghiệm thu chính:"
    )
    
    doc.add_heading("7.1. Kịch bản kiểm thử chuyển hướng HTTPS và SSL", level=2)
    doc.add_paragraph(
        "Kiểm thử gửi yêu cầu HTTP bình thường qua lệnh curl -s -I http://localhost:80:\n"
        "-> Kết quả: Máy chủ Nginx phản hồi mã 301 Moved Permanently, với tiêu đề Location: https://localhost/.\n"
        "Kiểm thử chứng chỉ SSL qua OpenSSL xác nhận cặp khóa RSA 2048-bit hợp lệ, hỗ trợ giao thức TLSv1.3 hiện đại "
        "và tích hợp đầy đủ tên miền thay thế trong phần mở rộng SAN."
    )
    
    doc.add_heading("7.2. Kịch bản kiểm thử Security Headers", level=2)
    doc.add_paragraph(
        "Gửi yêu cầu kiểm tra tiêu đề phản hồi qua lệnh curl -k -s -I https://localhost:443:\n"
        "-> Kết quả kiểm tra xác nhận đạt 100% các tiêu đề an ninh bắt buộc:\n"
        "- [PASS] X-Frame-Options: SAMEORIGIN\n"
        "- [PASS] X-Content-Type-Options: nosniff\n"
        "- [PASS] X-XSS-Protection: 1; mode=block\n"
        "- [PASS] Strict-Transport-Security: max-age=31536000; includeSubDomains; preload\n"
        "- [PASS] Referrer-Policy: strict-origin-when-cross-origin\n"
        "- [PASS] Content-Security-Policy: default-src 'self' ...\n"
        "- [PASS] Permissions-Policy: geolocation=(), microphone=(), camera=()"
    )
    
    doc.add_heading("7.3. Kịch bản kiểm thử Hardening chặn XML-RPC và File nhạy cảm", level=2)
    doc.add_paragraph(
        "Thực hiện giả lập hành vi tấn công dò quét:\n"
        "1. Gửi request vào https://localhost/xmlrpc.php -> Nginx trả về mã 403 Forbidden [PASS].\n"
        "2. Gửi request thăm dò tệp bí mật https://localhost/.env -> Nginx trả về mã 403 Forbidden [PASS].\n"
        "3. Gửi request vào thư mục chứa mã nguồn https://localhost/.git -> Nginx trả về mã 403 Forbidden [PASS]."
    )
    
    doc.add_heading("7.4. Kịch bản kiểm thử truy vấn LogQL trên Grafana Explore", level=2)
    doc.add_paragraph(
        "Khi thực hiện các yêu cầu gây lỗi trên, truy cập giao diện Grafana Explore với nguồn dữ liệu Loki "
        "và thực thi câu truy vấn LogQL: {job=\"nginx\"} |= \"403\".\n"
        "-> Kết quả: Toàn bộ các dòng log bị chặn kèm thông tin địa chỉ IP nguồn, thời điểm và URI yêu cầu "
        "được hiển thị chi tiết theo định dạng thời gian thực, chứng minh hệ thống Promtail và Loki hoạt động hoàn hảo."
    )
    
    doc.add_heading("7.5. Hướng dẫn vận hành và bảo trì hệ thống", level=2)
    doc.add_paragraph(
        "Quy trình vận hành chuẩn hóa cho quản trị viên:\n"
        "- Khởi động nhanh toàn bộ hệ thống: docker compose up -d (hoặc chạy script scripts/setup.ps1 / setup.sh).\n"
        "- Kiểm tra trạng thái sức khỏe: docker compose ps.\n"
        "- Chạy bộ kiểm thử tự động: powershell -ExecutionPolicy Bypass -File .\\scripts\\test-system.ps1.\n"
        "- Sao lưu cơ sở dữ liệu định kỳ: docker exec production-mysql mysqldump -u root -p wordpress_db > backup.sql.\n"
        "- Dừng toàn bộ hệ thống: docker compose down."
    )
    
    doc.add_page_break()
    
    # --- CHƯƠNG 8 ---
    doc.add_heading("CHƯƠNG 8: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", level=1)
    
    doc.add_heading("8.1. Các kết quả đã hoàn thành", level=2)
    doc.add_paragraph(
        "Đề tài đã hoàn thành xuất sắc và vượt mức toàn bộ các yêu cầu kỹ thuật do đề bài quy định:\n"
        "1. Đóng gói hoàn chỉnh ngăn xếp ứng dụng WordPress quảng bá sản phẩm, cơ sở dữ liệu MySQL 8.0 và công cụ quản trị phpMyAdmin.\n"
        "2. Thiết lập lớp Reverse Proxy Nginx mạnh mẽ với chuyển hướng HTTPS tự ký có SAN, bộ quy tắc bảo mật Security Headers và Rate Limiting.\n"
        "3. Tích hợp giải pháp quan sát toàn diện Prometheus + Grafana với cAdvisor, MySQL Exporter, Nginx Exporter và 3 Dashboards tự động nạp.\n"
        "4. Xây dựng hệ thống quản lý nhật ký tập trung Loki + Promtail và bộ 5 câu truy vấn LogQL chuyên sâu.\n"
        "5. Thực thi các biện pháp gia cố bảo mật Hardening (Non-root, Network Isolation, Least Privilege, Quản lý biến môi trường an toàn).\n"
        "6. Quản lý mã nguồn theo chuẩn Git với 4 commit tương ứng từng giai đoạn phát triển và tài liệu báo cáo khoa học hơn 10 trang."
    )
    
    doc.add_heading("8.2. Hạn chế và Hướng mở rộng", level=2)
    doc.add_paragraph(
        "Trong các giai đoạn phát triển tiếp theo, hệ thống có thể được nghiên cứu mở rộng:\n"
        "- Tích hợp module Certbot Let's Encrypt tự động phát hành và gia hạn chứng chỉ SSL hợp lệ khi triển khai tên miền công khai.\n"
        "- Chuyển dịch mô hình triển khai sang Kubernetes (K8s) với Ingress Controller và cơ chế tự động co giãn Pods (HPA) khi lưu lượng tăng cao.\n"
        "- Nhúng tường lửa ứng dụng chuyên sâu ModSecurity / Coraza WAF với bộ quy tắc OWASP Core Rule Set (CRS).\n"
        "- Cấu hình Prometheus Alertmanager tự động gửi cảnh báo khẩn cấp qua Telegram/Discord khi phát sinh sự cố quá tải."
    )
    
    doc.add_page_break()
    
    # --- TÀI LIỆU THAM KHẢO ---
    doc.add_heading("TÀI LIỆU THAM KHẢO", level=1)
    refs = [
        "1. Docker Documentation, 'Docker Compose File Reference & Best Practices for Production', 2026. [Online]. Available: https://docs.docker.com/compose/",
        "2. Nginx Documentation, 'Configuring NGINX as an HTTP Reverse Proxy & SSL Termination', 2026. [Online]. Available: https://nginx.org/en/docs/",
        "3. Prometheus Authors, 'Prometheus - Monitoring system & Time Series Database Architecture', 2026. [Online]. Available: https://prometheus.io/docs/",
        "4. Grafana Labs, 'Grafana Loki - Like Prometheus, but for Logs & LogQL Reference', 2026. [Online]. Available: https://grafana.com/docs/loki/latest/",
        "5. OWASP Foundation, 'OWASP Secure Headers Project & Web Security Testing Guide', 2026. [Online]. Available: https://owasp.org/www-project-secure-headers/",
        "6. WordPress Codex & Developer Resources, 'Hardening WordPress & Operating Behind Reverse Proxies', 2026. [Online]. Available: https://developer.wordpress.org/advanced-administration/security/hardening/",
        "7. Center for Internet Security (CIS), 'CIS Docker Benchmark for Security Configuration', Version 1.6.0, 2025."
    ]
    for r in refs:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.add_run(r)
        
    doc.save(output_path)
    print("[OK] Report DOCX successfully generated!")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(current_dir, "BÁO_CÁO_BÀI_TẬP_LỚN.docx")
    build_docx_report(out_file)
