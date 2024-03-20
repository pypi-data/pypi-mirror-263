import matplotlib.pyplot as plt
import platform
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 初始化图表和数据
fig, ax = plt.subplots()

'''
待完善：macos系统的尺寸怎么获取计算；
'''
def set_font():
    try:
        # 获取当前操作系统信息
        os_system = platform.system()
        if os_system == 'Darwin':
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 使用 macOS 系统自带的中文字体
        elif os_system == 'Windows':
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用 Windows 系统自带的中文字体
        '''
        font_paths = matplotlib.font_manager.findSystemFonts()
        if font_paths:
            plt.title(fontproperties=font_paths[0],size=14)
        '''
    except:
        print('呀！我已经努力搜索了，未找到字体路径，标签暂不能使用中文哦！')


###############################预设数据上限100条##############################
np.random.seed(0)
# 生成随机颜色值
colors = ['#' + ''.join(f'{i:02x}' for i in np.random.randint(0, 256, 3)) for _ in range(100)]
labs = []
sizes = []
explode = [0 for i in range(100)]

# 支持绘制折线图、条形图的数据
xx = []
yy = []

# 图表类型
charts_type = 'bar'

'''
图表类型：
    柱状图：'bar'
    折线图：'line'
    饼图：'pie'
'''

def set_charts_type(type='bar'):
    global charts_type
    charts_type = type


def add_data(x='', y=''):
    if charts_type == 'bar':
        xx.append(x)
        if y == '':
            yy.append(0)
        else:
            yy.append(y)
    elif charts_type == "line":
        xx.append(x)
        if y == '':
            yy.append(0)
        else:
            yy.append(y)
        plt.text(x, y, f'({x}, {y})', ha='center', va='bottom')
    elif charts_type == 'pie':
        sizes.append(y)
        labs.append(x)
    draw_plt()

def clear():
    global xx, yy, labs, sizes
    xx = []
    yy = []
    labs = []
    sizes = []


# 添加标题和标签
def set_title(title=''):
    plt.title(title)


def set_xlabel(x='x'):
    plt.xlabel(x)


def set_ylabel(y='y'):
    plt.ylabel(y)

'''
# 创建Tkinter主窗口实例
root = tk.Tk()
# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
del root
'''

'''
isblock：
    为True时，开启阻塞模式；
    为False时，开启非阻塞模式；
'''
default = 0
def draw_plt(color='blue'):
    global default
    '''
    # 设置窗口的位置（这里的坐标是以屏幕左上角为原点）
    if default == 0:
        fig = plt.gcf()  # get current figure
        width, height = fig.get_size_inches()
        # 如果需要以像素为单位，加上dpi的转换
        dpi = fig.dpi
        width_in_pixels = width * dpi
        height_in_pixels = height * dpi
        #计算中心位置，显示的默认位置为：屏幕中心位置
        x = (screen_width - width_in_pixels) // 2
        y = (screen_height - height_in_pixels) // 2
        fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
        default = 1
    '''
    if charts_type == 'bar':
        sns.barplot(x=xx, y=yy,color=color)
    elif charts_type == 'line':
        plt.plot(xx, yy,color=color)
        plt.scatter(xx, yy, color='black', label='数据点')
        plt.xticks(xx,xx)
        plt.yticks(yy,yy)
    elif charts_type == 'pie':
        plt.clf()  # 清空当前图形
        plt.pie(sizes, explode=explode[:len(sizes)], labels=labs, colors=colors[:len(sizes)], autopct='%1.1f%%',
                shadow=True, startangle=140)


def update():
    draw_plt()

def show(isblock=True):
    if isblock:
        plt.show(block=True)
    else:
        plt.ion()
        draw_plt()
        plt.pause(0.001)
        if plt.waitforbuttonpress(0.01):
            pass

def get_charts_size():
    # 获取当前figure对象
    fig = plt.gcf()  # get current figure
    print(fig)
    # 获取figure的尺寸（单位：英寸）
    width, height = fig.get_size_inches()
    # 如果需要以像素为单位，加上dpi的转换
    dpi = fig.dpi
    width_in_pixels = width * dpi
    height_in_pixels = height * dpi
    print(f"Figure size in inches: {width:.2f} x {height:.2f}")
    print(f"Figure size in pixels: {width_in_pixels:.2f} x {height_in_pixels:.2f}")


def close():
    plt.close()


set_font()
