	.file	"cdecl.c"
	.intel_syntax noprefix
	.text
	.globl	callee
	.type	callee, @function
callee:
	push	rbp
	mov	rbp, rsp
	mov	DWORD PTR [rbp-4], edi
	mov	DWORD PTR [rbp-8], esi
	nop
	pop	rbp
	ret
	.size	callee, .-callee
	.globl	caller
	.type	caller, @function
caller:
	push	rbp
	mov	rbp, rsp
	mov	esi, 2
	mov	edi, 1
	call	callee
	nop
	pop	rbp
	ret
	.size	caller, .-caller
	.ident	"GCC: (Debian 14.2.0-12) 14.2.0"
	.section	.note.GNU-stack,"",@progbits
