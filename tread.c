std::stread th_name(func_name,arg...)//线程向下执行，主程序已结束
th_name.join();//等待
th_name.detach();//分离子线程与主线程
th_name.joinable();//是否可以join
std::ref(a)//引用----栈问题----main空间和全局空间
//智能指针在多线程中多个线程指向一个内存
//入口函数为私有成员函数--友元
#include<mutex>//互斥锁
std::mutex mtx;
mtx.lock();
mtx.unlock();
//概念：线程安全--每次多线程和单线程结果一样
//互斥量死锁 先获得mtx1 去获得mtx2；
//weakptr的作用？
std::lock_guard<std::mutex> lg(mtx，（adoptlock已获取锁不用上）);//相当于安全上锁，析构时unlock mtx
//explict禁止隐式转换
//lockguard类禁用了构造复制以及op= （=delete）
std::unique_lock<std::time_mutex> ul(mtx);//加锁，有多重构造如不用加锁重载，多种方法消耗资源
ul.lock_for(time);//若等不到就不等了，返回0，等到了就返回1--返回bool值
//ul支持移动语义传递,也支持swap
//单例模式--日志类
//类内静态函数只能访问静态变量，函数内static声明?--首次遇到时初始化（直接提出来？直接变一阶段初始化？），之后便不再初始化（不执行该声明赋值语句）
std::call_once(std::once_flag, func, arg...)//只调用一次，单例模式new时


