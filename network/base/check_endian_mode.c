/*
 * 内存中存储字节格式的确定
 *		格式：
 *			小端地址：
 *				将低序字节存储在起始地址
 *			大端地址：
 *				将高序字节存储在起始地址
 *
 *		方法：
 *			使用联合体的特点，共用一个存储空间。将一个两个字节存储在联合体中，
 *			用内置的字节数组访问每个字节存储的值，从而确定是大端还是小端。
 */

#include <stdio.h>

int main(int argc, char **argv) {
	union {
		short s;
		char c[sizeof(short)];
	} un;

	un.s = 0x0102;

	if(sizeof(short) == 2) {
		if(un.c[0] == 1 && un.c[1] == 2) {
			printf("big endian\n");
		} else if(un.c[0] == 2 && un.c[1] == 1) {
			printf("little endian\n");
		} else {
			printf("unknown\n");
		}
	}

	return 0;
}
