import psutil
import socket
import subprocess
import time
import os
import wmi
import threading
import win32gui
import psutil
import re
import pygetwindow as gw
import win32process


def 重复线程检测(self, func):
    for thread in threading.enumerate():
        if thread.name == func.__name__:
            return True
    return False


def check_process_type(process_name):
    for proc in psutil.process_iter(["pid", "name", "username", "status"]):
        if proc.info["name"] == process_name:
            if proc.info["username"] == "NT AUTHORITY\\SYSTEM":
                return "以Windows服务运行"
            else:
                return "以用户交互界面运行"
    return f"进程列表中找不到该程序{process_name},可能未运行"


def get_top_window(debug=False):
    # log("# 获取最顶层程序的窗口句柄")
    hwnd = win32gui.GetForegroundWindow()
    # log("# 获取窗口标题from hwnd"+str(hwnd))
    if hwnd < 1:
        if debug:
            print("hwnd<1,return")
        time.sleep(1)
        return
    hwnd = hwnd[1] if isinstance(hwnd, list) else hwnd
    title = win32gui.GetWindowText(hwnd)

    # log("# 获取pidfrom hwnd"+str(hwnd))
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]

    # log("# 获取进程名from pid"+str(pid))
    process_name = psutil.Process(pid).name()
    # log("# 获取进程名finish")
    if debug:
        print("top win hwd=", hwnd, title, end=" ")
    return hwnd, title, process_name


def if_process_is_top(exe_name, debug=False):
    try:
        hwnd, window_title, process_name = get_top_window()
    except Exception as e:
        print("if_tdx_top:" + str(e))
        return
    # 判断窗口标题是否包含“通达信”且进程名为“tdx.exe”
    if exe_name.lower() in process_name.lower():
        if debug:
            print("通达信i is true")
        return True
    else:
        if debug:
            print("通达信 is false`" + window_title)
        return False


def xxx(exe_name, debug=False):
    if debug:
        print("enter if_process_is_top")
    for proc in psutil.process_iter(["pid", "name", "create_time", "cpu_percent"]):
        print(proc.info["name"])
        if proc.info["name"].lower() == exe_name.lower():
            if proc.info["pid"] == psutil.Process().pid:
                return True
            break
    return False


def open_directory(dir_name):
    subprocess.Popen(r"explorer " + dir_name)


def open_file_in_new_thread(filepath):

    def edit_file(filepath):
        subprocess.run(["notepad.exe", filepath])

    thread = threading.Thread(target=edit_file, args=(filepath,))
    thread.start()


def check_processes_and_notice(task_list, notice_func=None, debug=False):
    # 检查事先定义好的进程是否已经启动，如果没有启动，就执行指定的操作。
    if debug:
        print("enter check_processes")

    # 先取所有进程及子进程名字到一个集合里面。类似('updater.exe', 'hipsdaemon.exe', 'python.exe', 'tdxw.exe', 'dbsvr_abc.exe', 'atiesrxx.exe', 'comppkgsrv.exe', 'qqprotect.exe', 'mysqld.exe'...)
    all_set = get_all_process_with_child()
    result_dict = {}
    if debug:
        print(all_set)
    for to_check_process in task_list:
        if os.path.basename(to_check_process).lower() in all_set:
            result_dict[to_check_process] = True
    # result_dict = lyyprocess.get_result_dict_from_set(all_set, task_dict)

    if debug:
        print("result_dict", result_dict)
    # 把路径去掉。false_keys ['D:/Soft/_lyytools/_jiepan/_jiepan.exe', 'D:/Soft/_lyytools/f1999/f1999.exe']
    false_keys = [os.path.basename(key) for key in task_list if key not in result_dict.keys()]
    if debug:
        print("false_keys", false_keys)
    if false_keys and notice_func:
        notice_func(" 和 ".join(false_keys) + "未运行", "请及时检查")


def if_set_include_list_element(all_set, task_dict):
    """
    判断要检查的程序（在字典中的元素）是否被包含在全体进程集合中，从而不管是否子进程，都能正确找到。

    """
    print("all_set length=", len(all_set))
    result_dict = {}
    for item in all_set:
        found = False  # 标记是否找到匹配的任务
        for task in task_dict.keys():
            if task in item:
                result_dict[task] = True
                found = True
                break  # 只跳出当前的内部循环
        if found:
            continue  # 继续下一个外部循环
    return result_dict


def get_all_process_with_child():
    """
    获取当前运行的所有进程及子进程名字，存入集合中。
    """
    all_set = set()
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            process_name = proc_info["name"].lower()
            all_set.add(process_name)
            print("+", end="", flush=True)
            child_procs = psutil.Process(proc_info["pid"]).children(recursive=True)
            for child_proc in child_procs:
                child_proc_info = child_proc.as_dict(attrs=["pid", "name"])
                child_process_name = child_proc_info["name"].lower()
                all_set.add(child_process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return all_set


def get_all_process_hwnd_dict():
    """
    获取当前运行的所有进程及子进程名字，存入字典中。
    """
    hwnd_dict = {}
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            process_name = proc_info["name"].lower()

            if process_name not in hwnd_dict.keys():
                hwnd_dict[process_name] = proc_info["pid"]

            print("+", end="", flush=True)
            child_procs = psutil.Process(proc_info["pid"]).children(recursive=True)
            for child_proc in child_procs:
                child_proc_info = child_proc.as_dict(attrs=["pid", "name"])
                child_process_name = child_proc_info["name"].lower()
                if child_process_name not in hwnd_dict.keys():
                    hwnd_dict[child_process_name] = proc_info["pid"]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return hwnd_dict


def check_processes(task_dict):
    """
    检查指定的进程是否在运行，如果没有运行，打印出来，并返回。用来通知哪些没运行。
    """
    print("enter check_processes, try to find name in all process and child process")
    false_list = []
    all_set = get_all_process_with_child()
    result_dict = if_set_include_list_element(all_set, task_dict)
    print("result_dict", result_dict)
    false_keys = [key for key in task_dict.keys() if key not in result_dict.keys()]
    print("false_keys", false_keys)
    if false_keys:
        print(" 和 ".join(false_keys) + "未运行", "请及时检查")
    false_list = [x for x in false_keys if x in task_dict.keys()]
    return false_keys


def check_port_in_use(port):
    # 检查指定端口是否被占用
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("localhost", port))
        except OSError:
            print("# 端口被占用，查找占用端口的进程")
            for conn in psutil.net_connections():
                if conn.status == "LISTEN" and conn.laddr.port == port:
                    pid = conn.pid
                    process = psutil.Process(pid)
                    print(f"# 占用端口的进程名：{process.name()}，进程路径：{process.exe()}")
                    return process.name(), process.exe()
    return None, None


def kill_process_by_name(name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == name:
            proc.kill()


def terminate_process_using_port(port):
    try:
        command = f"netstat -ano | findstr :{port}"
        output = subprocess.check_output(command, shell=True, text=True)
        lines = output.strip().split("\n")
        for line in lines:
            parts = line.split()
            pid = int(parts[-1])
            subprocess.run(["taskkill", "/F", "/PID", str(pid)])
        print("已结束占用该端口的程序")
        return pid
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"结束占用该端口的程序时出现错误：{e}")
        return None


def run_with_error_handling(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        # 处理异常，可以打印日志或执行其他操作
        print(f"模块 {func.__name__} 出现异常: {e}")


def get_child_process_number(parent_name="JY-Main.exe", debug=False):
    parent_pid = None
    # 查找主进程
    for process in psutil.process_iter(["pid", "name", "cmdline"]):
        process_info = process.info
        if parent_name.lower() in process_info["name"].lower():
            parent_pid = process_info["pid"]
            break
        elif debug:
            print(process_info["name"])

    if parent_pid is None:
        print(f"没有找到名为 {parent_name} 的进程")
        return 0
    # print(f"找到名为 {parent_name} 的进程，其PID为 {parent_pid}")
    parent = psutil.Process(parent_pid)
    # 列举子进程
    children = parent.children()
    if children:
        for child in children:
            print(f"  PID: {child.pid}, 名称: {child.name()}")
    # 列举子线程

    # if main_thread:
    #     for thread_id, thread_obj in threading._active.items():
    #         if thread_obj.ident != main_thread.ident:
    #             #print(f"  Thread ID: {thread_obj.ident}")
    print("子线程数量为：", len(children))
    return len(children)


def get_hwnd(process_name, debug=False):
    for proc in psutil.process_iter(["pid", "name"]):
        if debug:
            print(proc.as_dict(attrs=["pid", "name"])["name"], process_name.lower())
        if debug:
            print(".", end="", flush=True)
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            if process_name.lower() in proc_info["name"].lower():

                pid = proc_info["pid"]
                if debug:
                    print("get the needed process, 要找的exe名字(", process_name + ")对应的pid=", pid)
                result = gw.getWindowsWithTitle(f"pid={pid}")
                if len(result) > 0:
                    hwnd = result[0].hwnd
                    return hwnd
            else:
                if debug:
                    print(".", end="", flush=True)
                # if debug: print("当前exe=",proc.as_dict(attrs=["pid", "name"])["name"],"需要找的exe=",process_name.lower() )
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None


def get_pid(process_name):
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            if process_name.lower() in proc_info["name"].lower():
                return proc_info["pid"]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def set_window_on_top(process):
    if process is not None:
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"已将进程 {process.pid} 置顶")
    else:
        print("未找到名为 'kingtrade' 的进程")


# 示例：将窗口句柄为12345的窗口放在最上层
import win32gui, win32con


def set_window_top(hwnd):
    print(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


# 获取指定句柄的窗口标题
def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)


# 根据窗口标题找到句柄，并置顶窗口
def find_and_set_top_window(title):
    # 当前看起来不生效。不得不用pywinauto
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and title in get_window_title(hwnd):
            set_window_top(hwnd)

    win32gui.EnumWindows(callback, None)


if __name__ == "__main__":

    time.sleep(3)
    print(if_process_is_top("tdxw.exe", debug=True))  # 应输出False，因为notepad不是活动窗口

    time.sleep(3333)

    print(check_port_in_use(3306))
    kill_process_by_name("notepad.exe")

    exit()
    task_dict = {"jiepan": "D:/Soft/_lyytools/_jiepan/_jiepan.exe", "gui-only": "D:/Soft/_lyytools/gui-only/gui-only.exe", "kingtrader": "D:/Soft/_Stock/KTPro/A.点我登录.exe"}
    stopped = check_processes(task_dict)
    print("stopped=", stopped)
