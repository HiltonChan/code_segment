/*************************************************************************
	> File Name: ready_compile.c
	> Author: xujianguo
	> Mail: ray_xujianguo@yeah.net 
	> Created Time: 2015年06月25日 星期四 22时16分59秒
 ************************************************************************/

/*
 * 宏：
 *		类型：
 *			无参数的宏：对程序中的宏标记用值进行替，如NAME
 *			带参数的宏：原理跟无参数的一样，替换到对应的位置中，如ADD
 *				带参的宏跟函数的却别：
 *					1.带参的宏进行直接的替换，不需要函数的调用，效率更高
 *					2.函数只需一次编译，多次使用，但是多处使用宏的话，替换时间开销会更加
 *		作用：
 *			1.高效率的替换，跟函数对比可以得出这个优点
 *			2.减少硬编码，更改一处即可
 *		
 * 条件编译：
 *		作用：
 *			1.通过条件判断需要编译的语句
 *			2.可以减少不必要的编译，加快速度
 *
 * ANSI C预定义的5个宏：
 *		__DATE__：当前源程序的创建日期
 *		__FILE__：当前源程序的文件名称
 *		__LINE__：当前被的行号
 *		__STDC__：编译器是否为ANSI C标准
 *		__TIME__：当前源程序的创建时间
 */

#include <stdio.h>

//无参数的宏
#define NAME "xujianguo"
//带参数的宏
#define ADD(x, y) (x+y)
//条件编译
#define AGE 21

int main() {
	//宏的测试
	printf("%s\n", NAME);
	printf("%d\n", ADD(1, 3));
	
	//条件编译的测试
	#if AGE < 10
		printf("author is child\n");
	#elif AGE < 30
		printf("author is teenager\n");
	#else
		printf("author is man\n");
	#endif

	#ifdef AGE
		printf("AGE is define\n");
	#else
		printf("AGE is not define\n");
	#endif
	
	//5个预定义宏的测试
	printf("date is %s\n", __DATE__);
	printf("time is %s\n", __TIME__);
	printf("filename is %s\n", __FILE__);
	printf("code line is %d\n", __LINE__);
	printf("belong to ansi c?%d\n", __STDC__);

	return 0;
}
