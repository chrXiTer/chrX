#coding: utf-8
"""

"""

from bottle import route, view, Bottle, request
from bottle import static_file
from bottle import redirect

from datetime import datetime
import os

app = Bottle()


htmlStr_1 = '''<div id="navsecond">
<div id="courseMenuKey">CSS3教程 菜单</div>
<div id="course">
<h2>CSS 基础教程</h2>
<ul>
<li><a href="../cssref/index.htm" title="CSS3 参考手册">**CSS3 参考手册</a></li>
<li><a href="css_intro.htm" title="CSS 简介">CSS 简介</a></li>
<li><a href="css_syntax.htm" title="CSS 基础语法"> 语法</a></li>
<li><a href="css_howto.htm" title="如何创建 CSS"> 创建</a></li>
</ul>
<h2>CSS 样式</h2>
<ul>
<li><a href="css_border_outline.htm" title="边框">边框/轮廓</a></li>
<li><a href="css_background.htm" title="背景">背景</a></li>
<li><a href="css_text.htm" title="文本效果">文本效果</a></li>
<li><a href="css_font.htm" title="字体">字体</a></li>
<li><a href="css3_2d_3dtransform.htm" title="2D/3D 转换">2D/3D 转换</a></li>
<li><a href="css3_transition.htm" title="过渡">过渡</a></li>
<li><a href="css3_animation.htm" title="动画">动画</a></li>
<li><a href="css3_multiple_columns.htm" title="多列">多列</a></li>
<li><a href="css3_user_interface.htm" title="用户界面">用户界面</a></li>
<li><a href="css_list.htm" title="列表">列表</a></li>
<li><a href="css_table.htm" title="表格">表格</a></li>
<li><a href="css_dimension.htm" title="尺寸">尺寸</a></li>
<li><a href="css_mediatypes.htm" title="媒介类型">媒介类型</a></li>
<li><a href="csse_examples.htm" title="CSS 实例">CSS 实例练习</a></li>
</ul>
<h2><a href="css_boxmodel.htm" title="CSS 盒模型">CSS 盒模型</a></h2>
<ul>
<li><a href="css_padding.htm" title="CSS 内边距">内边距</a></li>
<li><a href="css_margin.htm" title="CSS 外边距">外边距</a></li>
<li><a href="css_margin_collapsing.htm" title="CSS 外边距合并">外边距合并</a></li>
</ul>
<h2><a href="css_positioning.htm" title="CSS 定位概述">CSS 定位／布局</a></h2>
<ul>
<li><a href="css_positioning_relative.htm" title="相对定位">相对定位</a></li>
<li><a href="css_positioning_absolute.htm" title="绝对定位">绝对定位</a></li>
<li><a href="css_positioning_floating.htm" title="浮动">浮动</a></li>
</ul>
<h2>CSS 选择器</h2>
<ul>
<li><a href="css_selector_type.htm" title="元素选择器">元素选择器</a></li>
<li><a href="css_selector_grouping.htm" title="选择器分组">选择器分组</a></li>
<li><a href="css_selector_derive.htm" title="派生选择器">派生选择器</a></li>
<li><a href="css_selector_descendant.htm" title="后代选择器">后代选择器</a></li>
<li><a href="css_selector_child.htm" title="子元素选择器">子元素选择器</a></li>
<li><a href="css_selector_adjacent_sibling.htm" title="相邻兄弟选择器">相邻兄弟选择器</a></li>
<li><a href="css_selector_class.htm" title="类选择器">类选择器</a></li>
<li><a href="css_selector_id.htm" title="ID 选择器详解">ID 选择器详解</a></li>
<li><a href="css_selector_attribute.htm" title="属性选择器">属性选择器</a></li>
<li><a href="css_pseudo_classes_&_pseudo_elements.htm" title="伪类、伪元素">伪类、伪元素</a></li>
</ul>
</div>


</div>'''

htmlStr_2 = '''<div id="navsecond">
<div id="courseMenuKey">CSS3参考 菜单</div>
<div id="course">
<h2>CSS 参考手册</h2>
<ul>
<li><a href="../css/css_intro.htm" title="CSS 简介">**CSS 教程</a></li>
<li><a href="index.htm" title="CSS3 参考手册">CSS3 参考手册</a></li>
<li><a href="css_selectors.htm" title="CSS 选择器参考手册">CSS 选择器</a></li>
<li><a href="css_ref_aural.htm" title="CSS 听觉参考手册">CSS 听觉参考手册</a></li>
<li><a href="css_websafe_fonts.htm" title="CSS 网络安全字体组合">CSS 网络安全字体</a></li>
<li><a href="css_units.htm" title="CSS 单位">CSS 单位</a></li>
<li><a href="css_colors_legal.htm" title="CSS 合法颜色值">CSS 颜色值</a></li>
</ul>
</div>
</div>'''

htmlStr_3 = '''<div id="navsecond">
<div id="courseMenuKey">HTML5教程 菜单</div>
<div id="course">
<h2>HTML 基础</h2>
<ul>
<li><a href="../tags/html_ref_byfunc.htm"  title="HTML参考手册">**HTML标签列表</a></li>
<li><a href="../tags/index.htm"  title="HTML参考手册">**HTML参考</a></li>
<li><a href="html_intro.htm"  title="简介">简介</a></li>
<li><a href="html_elements.htm"  title="元素">元素</a></li>
<li><a href="html_attributes.htm"  title="属性"> 属性</a></li>
<li><a href="html_basic.htm"  title="基础 - 四个实例"> 基础</a></li>
<li><a href="html_links.htm"  title="链接"> 链接</a></li>
<li><a href="html_blocks.htm"  title="&lt;div&gt; 和 &lt;span&gt;"> 块</a></li>
<li><a href="html_tables.htm"  title=" 表格"> 表格</a></li>
<li><a href="html_lists.htm"  title="列表"> 列表</a></li>
<li><a href="html_css.htm"  title="样式 - CSS"> 样式</a></li>
<li><a href="html_formatting.htm"  title="文本格式化"> 格式</a></li>
<li><a href="html_layout.htm"  title="布局"> 布局</a></li>
<li><a href="html_doctype.htm"  title="&lt;!DOCTYPE&gt;"> 文档类型</a></li>
<li><a href="html_head.htm"  title="头部元素">头部</a></li>
<li><a href="html_scripts.htm"  title="脚本">脚本</a></li>
<li><a href="html_entities.htm"  title="字符实体/转义">字符实体/转义</a></li>
<li><a href="html_url.htm"  title="统一资源定位器"> URL</a></li>
<li><a href="html_forms.htm"  title="表单和输入"> 表单</a></li>
<li><a href="html_frames.htm"  title="框架"> 框架</a></li>
<li><a href="html_media.htm"  title="多媒体 & Object"> 媒体_对象</a></li>
<li><a href="html_audio.htm"  title="音频"> 音频</a></li>
<li><a href="html_video.htm"  title="视频"> 视频</a></li>
<li>---<li>
<li><a href="htmle_examples.htm"  title="HTML 实例"> 实例</a></li>
</ul>
<h2>HTML5 教程</h2>
<ul>
<li><a href="html_5_video.htm" title="视频"> 视频</a></li>
<li><a href="html_5_audio.htm" title="音频"> 音频</a></li>
<li><a href="html_5_draganddrop.htm"  title="拖放">拖放</a></li>
<li><a href="html_5_canvas.htm" title="Canvas">画布</a></li>
<li><a href="html_5_svg.htm" title="内联 SVG">SVG</a></li>
<li><a href="html_5_canvas_vs_svg.htm" title="Canvas vs. SVG">画布 vs SVG</a></li>
<li><a href="html_5_file.htm"  title="文件">文件</a></li>
<li><a href="html_5_geolocation.htm" title="地理定位">地理定位</a></li>
<li><a href="html_5_webstorage.htm" title="Web 存储">Web 存储</a></li>
<li><a href="html_5_app_cache.htm" title="应用程序缓存">应用缓存</a></li>
<li><a href="html_5_webworkers.htm" title="Web Workers">Web Workers</a></li>
<li><a href="html_5_serversentevents.htm" title="服务器发送事件">服务器发送事件</a></li>
</ul>
<h2>HTML5 表单</h2>
<ul>
<li><a href="html_5_form_input_types.htm"  title="input 类型">输入类型</a></li>
<li><a href="html_5_form_elements.htm"  title="表单元素">表单元素</a></li>
<li><a href="html_5_form_attributes.htm"  title="表单属性">表单属性</a></li>
</ul>
<h2><a href="html_xhtml.htm"  title="XHTML">XHTML</a></h2>
</div>
</div>'''

htmlStr_4 = '''<div id="navsecond">
<div id="courseMenuKey">HTML5参考 菜单</div>
<div id="course"><h2>参考手册</h2>
<ul>
<li><a href="../html/html_intro.htm"  title="HTML教程">**HTML教程</a></li>
<li><a href="index.htm"  title="HTML5参考手册">HTML标签*字母排序</a></li>
<li><a href="html_ref_byfunc.htm"  title="HTML5参考手册byfunc">HTML标签*功能排序</a></li>
<li><a href="html_ref_dtd.htm"  title="HTML 元素和有效的 DTD">HTML标签 文档类型</a></li>
<li><a href="html_ref_standardattributes.htm"  title="HTML 标准属性">HTML 属性</a></li>
<li><a href="html_ref_eventattributes.htm"  title="HTML 事件属性">HTML 事件</a></li>
<li>---</li>
<li><a href="html_ref_audio_video_dom.htm"  title="HTML Audio/Video DOM 属性">HTML 视频/音频</a></li>
<li><a href="html_ref_canvas.htm"  title="HTML Canvas 参考手册">HTML 画布</a></li>
<li>---</li>
<li><a href="html_ref_colornames.htm"  title="HTML 颜色名">HTML 颜色名</a></li>
<li><a href="html_ref_charactersets.htm"  title="HTML 字符集">HTML 字符集</a></li>
<li><a href="html_ref_ascii.htm"  title="HTML 7 比特 ASCII 代码 参考手册">HTML ASCII</a></li>
<li><a href="html_ref_entities.html"  title="HTML ISO-8859-1 参考手册">HTML ISO-8859-1</a></li>
<li><a href="html_ref_symbols.html"  title="HTML 符号实体">HTML 符号</a></li>
<li><a href="html_ref_urlencode.html"  title="HTML URL 编码">HTML URL 编码</a></li>
<li><a href="html_ref_language_codes.htm"  title="HTML 语言代码参考手册">HTML 语言代码</a></li>
<li><a href="html_ref_httpmessages.htm"  title="HTTP 状态消息">HTTP 消息</a></li>
<li><a href="html_ref_httpmethods.htm"  title="HTTP 方法：GET 对比 POST">HTTP 方法</a></li>
</ul>
</div>

</div>'''

htmlStr_5 = '''<div id="navsecond">
<div id="courseMenuKey">JavaScript教程 菜单</div>
<div id="course"><h2>JS 教程</h2>
<ul>
<li><a href="../jsref/index.htm"  title="JavaScript 参考手册">**JS 参考</a></li>
<li><a href="js_intro.htm"  title="JavaScript 简介"> 简介</a></li>
<li><a href="js_howto.htm"  title="JavaScript 实现"> 实现</a></li>
<li><a href="js_whereto.htm"  title="JavaScript 输出"> 输出</a></li>
<li><a href="js_statements.htm"  title="JavaScript 语法介绍"> 语法介绍</a></li>
<li><a href="js_variables.htm"  title="JavaScript 变量"> 变量</a></li>
<li><a href="js_datatypes.htm"  title="JavaScript 数据类型"> 数据类型</a></li>
<li><a href="pro_js_typeconversion.htm"  title="JavaScript 类型转换"> 类型转换</a></li>
<li><a href="js_functions.htm"  title="JavaScript 函数"> 函数</a></li>
<li><a href="js_obj_intro.htm"  title="JavaScript 对象"> 对象</a></li>
<li><a href="js_operators.htm"  title="JavaScript 运算符"> 运算符</a></li>
<li><a href="js_condition.htm"  title="JavaScript 条件语句">条件语句</a></li>
<li><a href="js_loop.htm"  title="JavaScript 循环">循环</a></li>
<li><a href="js_errors.htm"  title="JavaScript 错误 - Throw 和 try...catch"> 错误处理</a></li>
</ul>
<h2><a href="js_objects.htm"  title="JavaScript 对象">JS 对象</a></h2>
<ul>
<li><a href="js_obj_global.htm"  title="JavaScript 全局对象">全局对象</a></li>
<li><a href="js_obj_number.htm"  title="JavaScript Number 对象">数字</a></li>
<li><a href="js_obj_string.htm"  title="JavaScript String 对象">字符串</a></li>
<li><a href="js_obj_date.htm"  title="JavaScript Date 对象">日期</a></li>
<li><a href="js_obj_array.htm"  title="JavaScript Array 对象">数组</a></li>
<li><a href="js_obj_boolean.htm"  title="JavaScript Boolean 对象">逻辑</a></li>
<li><a href="js_obj_math.htm"  title="JavaScript Math 对象">算数</a></li>
<li><a href="js_obj_regexp.htm"  title="JavaScript RegExp 对象">正则表达式</a></li>
<li><a href="js_obj_function.htm"  title="function 对象">function</a></li>
<li><a href="js_obj_JSON.htm"  title="JSON 对象">JSON</a></li>
</ul>
<h2>JS window</h2>
<ul>
<li><a href="js_window.htm"  title="JavaScript window - 浏览器对象模型"> window</a></li>
<li><a href="js_window_screen.htm"  title="JavaScript window screen"> screen</a></li>
<li><a href="js_window_location.htm"  title="JavaScript window location"> location</a></li>
<li><a href="js_window_history.htm"  title="JavaScript window history"> history</a></li>
<li><a href="js_window_navigator.htm"  title="JavaScript window navigator"> navigator</a></li>
<li><a href="js_popup.htm"  title="JavaScript Popup Box"> PopupAlert</a></li>
<li><a href="js_timing.htm"  title="JavaScript Timing 事件"> Timing</a></li>
<li><a href="js_cookies.htm"  title="JavaScript cookies"> cookies</a></li>
</ul>
<h2><a href="js_htmldom.htm" title="JavaScript HTML DOM">JS HTML DOM</a></h2>
<ul>
<li><a href="js_htmldom_html.htm"  title="JavaScript HTML DOM - 改变 HTML">DOM HTML</a></li>
<li><a href="js_htmldom_css.htm"  title="JavaScript HTML DOM - 改变 CSS">DOM CSS</a></li>
<li><a href="js_htmldom_events.htm"  title="JavaScript HTML DOM 事件">DOM 事件</a></li>
<li><a href="js_htmldom_elements.htm"  title="JavaScript HTML DOM 元素（节点）">DOM 节点</a></li>
</ul>
<h2>JSON </h2>
<ul>
<li><a href="json_index.htm"  title="JSON 教程">JSON 教程</a></li>
<li><a href="json_intro.htm"  title="JSON 简介">JSON 简介</a></li>
<li><a href="json_syntax.htm"  title="JSON 语法">JSON 语法</a></li>
<li><a href="json_eval.htm"  title="JSON 使用">JSON 使用</a></li>
</ul>
<h2><a href="ajax_xmlhttprequest_create.htm"  title="AJAX">AJAX</a></h2>
<ul>
<li><a href="ajax_xmlhttprequest_send.htm"  title="AJAX 向服务器发送请求">XHR 请求</a></li>
<li><a href="ajax_xmlhttprequest_response.htm"  title="AJAX 服务器响应">XHR 响应</a></li>
<li><a href="ajax_xmlhttprequest_onreadystatechange.htm" title="AJAX onreadystatechange 事件">XHR readyState</a></li>
</ul>
<h2>其他</h2>
<ul>
<li><a href="js_form_validation.htm"  title="JavaScript 表单验证">JS 进行表单验证</a></li>
<li><a href="index_pro.htm"  title="JavaScript 高级教程">JS 高级教程</a></li>
</ul>
</div>

</div>'''

htmlStr_6 = '''<div id="navsecond">
<div id="courseMenuKey">JavaScript参考 菜单</div>
<div id="course">
<h2>JavaScript 核心</h2>
<ul>
<li><a href="../js/index.htm"  title="JavaScript 教程">**JS 教程</a></li>
<li><a href="jsref_obj_global.htm"  title="JavaScript 全局对象参考手册">JS 全局</a></li>
<li><a href="jsref_obj_array.htm"  title="JavaScript Array 对象参考手册">JS Array</a></li>
<li><a href="jsref_obj_boolean.htm"  title="JavaScript Boolean 对象参考手册">JS Boolean</a></li>
<li><a href="jsref_obj_date.htm"  title="JavaScript Date 对象参考手册">JS Date</a></li>
<li><a href="jsref_obj_math.htm"  title="JavaScript Math 对象的参考手册">JS Math</a></li>
<li><a href="jsref_obj_number.htm"  title="JavaScript Number 对象参考手册">JS Number</a></li>
<li><a href="jsref_obj_string.htm"  title="JavaScript String 对象参考手册">JS String</a></li>
<li><a href="jsref_obj_regexp.htm"  title="JavaScript RegExp 对象参考手册">JS RegExp</a></li>
</ul>
<h2>Browser 对象(BOM)</h2>
<ul>
<li><a href="bom_window.htm"  title="HTML DOM window 对象">window</a></li>
<li><a href="bom_navigator.htm"  title="HTML DOM navigator 对象">navigator</a></li>
<li><a href="bom_screen.htm"  title="HTML DOM screen 对象">screen</a></li>
<li><a href="bom_history.htm"  title="HTML DOM history 对象">history</a></li>
<li><a href="bom_location.htm"  title="HTML DOM location 对象">location</a></li>
</ul>
<h2>HTML DOM 对象</h2>
<ul>
<li><a href="dom_document.htm"  title="HTML DOM document 对象">DOM Document</a></li>
<li><a href="dom_all.htm"  title="HTML DOM element 对象">DOM Element</a></li>
<li><a href="dom_attributes.htm"  title="HTML DOM attribute 对象">DOM Attribute</a></li>
<li><a href="dom_event.htm"  title="HTML DOM event 对象">DOM Event</a></li>
</ul>
</div>

</div>'''

htmlStr_svg = '''<div id="navsecond">
<div id="courseMenuKey">SVG 菜单</div>
<div id="course">
<h2><a href="svg_intro.htm"  title="SVG 简介">SVG 简介</a></h2>
<h2>SVG 形状</h2>
<ul>
<li><a href="svg_rect.htm"  title="SVG &lt;rect&gt;">SVG 矩形</a></li>
<li><a href="svg_circle.htm"  title="SVG &lt;circle&gt;">SVG 圆形</a></li>
<li><a href="svg_ellipse.htm"  title="SVG &lt;ellipse&gt;">SVG 椭圆</a></li>
<li><a href="svg_line.htm"  title="SVG &lt;line&gt;">SVG 线条</a></li>
<li><a href="svg_polygon.htm"  title="SVG &lt;polygon&gt;">SVG 多边形</a></li>
<li><a href="svg_polyline.htm"  title="SVG &lt;polyline&gt;">SVG 折线</a></li>
<li><a href="svg_path.htm"  title="SVG &lt;path&gt;">SVG 路径</a></li>
</ul>
<h2>SVG 滤镜</h2>
<ul>
<li><a href="svg_filters_intro.htm"  title="SVG 滤镜">SVG 滤镜简介</a></li>
<li><a href="svg_filters_gaussian.htm"  title="SVG 高斯滤镜">SVG 高斯滤镜</a></li>
</ul>
<h2>SVG 渐变</h2>
<ul>
<li><a href="svg_grad_linear.htm"  title="SVG 线性渐变">SVG 线性渐变</a></li>
<li><a href="svg_grad_radial.htm"  title="SVG 放射性渐变">SVG 放射渐变</a></li>
</ul>
<h2><a href="svg_examples.htm"  title="SVG 实例">SVG 实例</a></h2>
<h2><a href="svg_reference.htm"  title="SVG 参考手册">SVG 元素参考</a></h2>
</div>
</div>'''

htmlStr_sql = '''<div id="navsecond">
<div id="courseMenuKey">SQL 菜单</div>
<div id="course">
<h2>SQL 基础教程</h2>
<ul>
<li><a href="sql_intro.htm"  title="SQL 简介">SQL 简介</a></li>
<li><a href="sql_syntax.htm"  title="SQL 语法">SQL 语法</a></li>
<li><a href="sql_select.htm"  title="SQL SELECT 语句">SQL select</a></li>
<li><a href="sql_distinct.htm"  title="SQL SELECT DISTINCT 语句">SQL distinct</a></li>
<li><a href="sql_where.htm"  title="SQL WHERE 子句">SQL where</a></li>
<li><a href="sql_and_or.htm"  title="SQL AND &amp; OR">SQL AND &amp; OR</a></li>
<li><a href="sql_orderby.htm"  title="SQL ORDER BY 语句">SQL Order By</a></li>
<li><a href="sql_insert.htm"  title="SQL INSERT INTO 语句">SQL insert</a></li>
<li><a href="sql_update.htm"  title="SQL UPDATE 语句">SQL update</a></li>
<li><a href="sql_delete.htm"  title="SQL DELETE 语句">SQL delete</a></li>
</ul>
<h2>SQL 高级教程</h2>
<ul>
<li><a href="sql_top.htm"  title="SQL TOP 子句">SQL Top</a></li>
<li><a href="sql_like.htm"  title="SQL LIKE 运算符">SQL Like</a></li>
<li><a href="sql_wildcards.htm"  title="SQL 通配符">SQL 通配符</a></li>
<li><a href="sql_in.htm"  title="SQL IN">SQL In</a></li>
<li><a href="sql_between.htm"  title="SQL BETWEEN">SQL Between</a></li>
<li><a href="sql_alias.htm"  title="SQL Alias（别名）">SQL Aliases</a></li>
<li><a href="sql_join.htm"  title="SQL JOIN">SQL Join</a></li>
<li><a href="sql_join_inner.htm"  title="SQL INNER JOIN 关键字">SQL Inner Join</a></li>
<li><a href="sql_join_left.htm"  title="SQL LEFT JOIN 关键字">SQL Left Join</a></li>
<li><a href="sql_join_right.htm"  title="SQL RIGHT JOIN 关键字">SQL Right Join</a></li>
<li><a href="sql_join_full.htm"  title="SQL FULL JOIN 关键字">SQL Full Join</a></li>
<li><a href="sql_union.htm"  title="SQL UNION 和 UNION ALL">SQL Union</a></li>
<li><a href="sql_select_into.htm"  title="SQL SELECT INTO 语句">SQL Select Into</a></li>
<li><a href="sql_create_db.htm"  title="SQL CREATE DATABASE 语句">SQL Create DB</a></li>
<li><a href="sql_create_table.htm"  title="SQL CREATE TABLE 语句">SQL Create Table</a></li>
<li><a href="sql_constraints.htm"  title="SQL 约束">SQL Constraints</a></li>
<li><a href="sql_notnull.htm"  title="SQL NOT NULL 约束">SQL Not Null</a></li>
<li><a href="sql_unique.htm"  title="SQL UNIQUE 约束">SQL Unique</a></li>
<li><a href="sql_primarykey.htm"  title="SQL PRIMARY KEY 约束">SQL Primary Key</a></li>
<li><a href="sql_foreignkey.htm"  title="SQL FOREIGN KEY 约束">SQL Foreign Key</a></li>
<li><a href="sql_check.htm"  title="SQL CHECK 约束">SQL Check</a></li>
<li><a href="sql_default.htm"  title="SQL DEFAULT 约束">SQL Default</a></li>
<li><a href="sql_create_index.htm"  title="SQL CREATE INDEX 语句">SQL Create Index</a></li>
<li><a href="sql_drop.htm"  title="SQL 撤销索引、表以及数据库">SQL Drop</a></li>
<li><a href="sql_alter.htm"  title="SQL ALTER TABLE">SQL Alter</a></li>
<li><a href="sql_autoincrement.htm"  title="SQL AUTO INCREMENT 字段">SQL Increment</a></li>
<li><a href="sql_view.htm"  title="SQL VIEW（视图）">SQL View</a></li>
<li><a href="sql_dates.htm"  title="SQL Date 函数">SQL Date</a></li>
<li><a href="sql_null_values.htm"  title="SQL NULL 值">SQL Nulls</a></li>
<li><a href="sql_isnull.htm"  title="SQL NULL 函数">SQL isnull()</a></li>
<li><a href="sql_datatypes.htm"  title="SQL 数据类型">SQL 数据类型</a></li>
<li><a href="sql_server.htm"  title="SQL 服务器 - RDBMS">SQL 服务器</a></li>
</ul>
<h2>SQL 函数</h2>
<ul>
<li><a href="sql_functions.htm"  title="SQL 函数">SQL functions</a></li>
<li><a href="sql_func_avg.htm"  title="SQL AVG() 函数">SQL avg()</a></li>
<li><a href="sql_func_count.htm"  title="SQL COUNT() 函数">SQL count()</a></li>
<li><a href="sql_func_first.htm"  title="SQL FIRST() 函数">SQL first()</a></li>
<li><a href="sql_func_last.htm"  title="SQL LAST() 函数">SQL last()</a></li>
<li><a href="sql_func_max.htm"  title="SQL MAX() 函数">SQL max()</a></li>
<li><a href="sql_func_min.htm"  title="SQL MIN() 函数">SQL min()</a></li>
<li><a href="sql_func_sum.htm"  title="SQL SUM() 函数">SQL sum()</a></li>
<li><a href="sql_groupby.htm"  title="SQL GROUP BY 语句">SQL Group By</a></li>
<li><a href="sql_having.htm"  title="SQL HAVING 子句">SQL Having</a></li>
<li><a href="sql_func_ucase.htm"  title="SQL UCASE() 函数">SQL ucase()</a></li>
<li><a href="sql_func_lcase.htm"  title="SQL LCASE() 函数">SQL lcase()</a></li>
<li><a href="sql_func_mid.htm"  title="SQL MID() 函数">SQL mid()</a></li>
<li><a href="sql_func_len.htm"  title="SQL LEN() 函数">SQL len()</a></li>
<li><a href="sql_func_round.htm"  title="SQL ROUND() 函数">SQL round()</a></li>
<li><a href="sql_func_now.htm"  title="SQL NOW() 函数">SQL now()</a></li>
<li><a href="sql_func_format.htm"  title="SQL FORMAT() 函数">SQL format()</a></li>
<li><a href="sql_quickref.htm"  title="SQL 快速参考">SQL 快速参考</a></li>
</ul>
</div>
</div>'''

def htmlFileToString(path):
    file_object = open(path)
    all_the_text = "file not foundn"
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()

    if path.find('/tiy/') >=0:
        return all_the_text

    if path.find('/css/') >= 0:
        htmlStr = htmlStr_1
    elif path.find('/cssref/') >= 0:
        htmlStr = htmlStr_2
    elif path.find('/html/') >= 0:
        htmlStr = htmlStr_3
    elif path.find('/tags/') >= 0:
        htmlStr = htmlStr_4
    elif path.find('/js/') >= 0:
        htmlStr = htmlStr_5
    elif path.find('/jsref/') >= 0:
        htmlStr = htmlStr_6
    elif path.find('/svg/') >= 0:
        htmlStr = htmlStr_svg
    elif path.find('/sql/') >= 0:
        htmlStr = htmlStr_sql
    else:
        htmlStr = htmlStr_1

    all_the_text = all_the_text.replace('''<link rel="stylesheet" type="text/css" href="../c3.css" />''', '')
    all_the_text = all_the_text.replace('''<script src="../chrX.js"></script>''','''<script src="../chrXs.js"></script>''')
    all_the_text = all_the_text.replace('''<div id="wrapper">''',  '<div id="wrapper">\n' + htmlStr)
    return all_the_text

@app.route('/')
def callback():
    return redirect('/html/html_intro.htm')

@app.route('/static/<title_:path>')
def home():
    return "static"

@app.route('/tiy/<fileName>')
def tiy(fileName):
    return static_file(fileName, root='static/tiy')

@app.route('<filPath:path>')
@view("htmlFile")
def callback(filPath):
    if filPath.find('.htm') >= 0 or filPath.find('.html') >= 0:
        return dict(
            title = filPath,
            htmlContent = htmlFileToString('static' + filPath )
        )
    return static_file(filPath, root='static')








