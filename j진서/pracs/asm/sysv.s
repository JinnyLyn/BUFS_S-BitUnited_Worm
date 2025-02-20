	.file	"sysv.c"
	.intel_syntax noprefix
	.text
	.globl	callee
	.type	callee, @function
callee:
	push	rbp
	mov	rbp, rsp
	mov	QWORD PTR [rbp-24], rdi
	mov	DWORD PTR [rbp-28], esi
	mov	DWORD PTR [rbp-32], edx
	mov	DWORD PTR [rbp-36], ecx
	mov	DWORD PTR [rbp-40], r8d
	mov	DWORD PTR [rbp-44], r9d
	mov	eax, DWORD PTR [rbp-28]
	movsx	rdx, eax
	mov	rax, QWORD PTR [rbp-24]
	add	rdx, rax
	mov	eax, DWORD PTR [rbp-32]
	cdqe
	add	rdx, rax
	mov	eax, DWORD PTR [rbp-36]
	cdqe
	add	rdx, rax
	mov	eax, DWORD PTR [rbp-40]
	cdqe
	add	rdx, rax
	mov	eax, DWORD PTR [rbp-44]
	cdqe
	add	rdx, rax
	mov	eax, DWORD PTR [rbp+16]
	cdqe
	add	rax, rdx
	mov	QWORD PTR [rbp-8], rax
	mov	rax, QWORD PTR [rbp-8]
	pop	rbp
	ret
	.size	callee, .-callee
	.globl	caller
	.type	caller, @function
caller:
	push	rbp
	mov	rbp, rsp
	push	7
	mov	r9d, 6
	mov	r8d, 5
	mov	ecx, 4
	mov	edx, 3
	mov	esi, 2
	movabs	rax, 123456789123456789
	mov	rdi, rax
	call	callee
	add	rsp, 8
	nop
	leave
	ret
	.size	caller, .-caller
	.globl	main
	.type	main, @function
main:
	push	rbp
	mov	rbp, rsp
	mov	eax, 0
	call	caller
	mov	eax, 0
	pop	rbp
	ret
	.size	main, .-main
	.ident	"GCC: (Debian 14.2.0-12) 14.2.0"
	.section	.note.GNU-stack,"",@progbits
