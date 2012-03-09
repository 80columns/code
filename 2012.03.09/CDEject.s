.STR1:  .string "/dev/cdrom"
.STR2:  .string "Error opening cd-rom device\n"
.STR3:  .string "Error performing eject operation on cd-rom device\n"
.STR4:  .string "Error closing cd-rom device\n"
.STR5:  .string ""

.globl main
main:
    push %rbp           # Function Prologue
    mov %rsp, %rbp      # Function Prologue
    mov $00004000, %rsi # Move 00004000 (O_RDONLY | O_NONBLOCK) into the
                        # second argument for the open() system call
    mov $.STR1, %rdi    # Move the string "/dev/cdrom" into the first
                        # argument for the open() system call
    mov $0, %rax        # Move 0 into rax
    call open           # Call the open() system call in order to open
                        # the cdrom device
    mov %rax, %r8       # Move open()'s return value into r8
    cmp $-1, %r8        # Compare open()'s return value to -1
    je .erropen         # If open()'s return value is -1, jump to the
                        # error message printing routine
    mov $21257, %rsi    # Move 21257 (CDROMEJECT) into the second
                        # argument for the ioctl() system call in order
                        # to eject the cd-rom drive
    mov %r8, %rdi       # Move the file descriptor for the cd-rom device
                        # into the first argument for the ioctl() system
                        # call
    mov $0, %rax        # Move 0 into rax
    call ioctl          # Call the ioctl() system call in order to eject
                        # the cdrom device
    cmp $-1, %rax       # Compare ioctl()'s return value to -1
    je .errioctl        # If ioctl()'s return value is -1, jump to the
                        # error message printing routine
    mov %r8, %rdi       # Move the file descriptor for the cd-rom device
                        # into the first argument for the close() system
                        # call
    mov $0, %rax        # Move 0 into rax
    call close          # Call the close() system call in order to close
                        # the cd-rom file descriptor
    cmp $-1, %rax       # Compare close()'s return value to -1
    je .errclose        # If close()'s return value is -1, jump to the
                        # error message printing routine
    mov $0, %rax        # Move 0 into rax for return value
    jmp .exit           # Jump to the exit label

.erropen:
    mov $.STR2, %rdi    # Move the open() error message string into the
                        # first argument for printf()
    mov $0, %rax        # Move 0 into rax
    call printf         # Call printf() to print the error message
    mov $.STR5, %rdi    # Move the string "" into the first argument
                        # for the perror() system call
    mov $0, %rax        # Move 0 into rax
    call perror         # Call the perror() system call to show what
                        # went wrong
    mov $1, %rax        # Move 1 into rax to return 1 to the shell as an
                        # error status
    jmp .exit           # Jump to the exit label

.errioctl:
    mov $.STR3, %rdi    # Move the ioctl() error message string into the
                        # first argument for printf()
    mov $0, %rax        # Move 0 into rax
    call printf         # Call printf() to print the error message
    mov $.STR5, %rdi    # Move the string "" into the first argument
                        # for the perror() system call
    mov $0, %rax        # Move 0 into rax
    call perror         # Call the perror() system call to show what
                        # went wrong
    mov $2, %rax        # Move 2 into rax to return 2 to the shell as an
                        # error status
    jmp .exit           # Jump to the exit label

.errclose:
    mov $.STR4, %rdi    # Move the close() error message string into the
                        # first argument for printf()
    mov $0, %rax        # Move 0 into rax
    call printf         # Call printf() to print the error message
    mov $.STR5, %rdi    # Move the string "" into the first argument
                        # for the perror() system call
    mov $0, %rax        # Move 0 into rax
    call perror         # Call the perror() system call to show what
                        # went wrong
    mov $3, %rax        # Move 3 into rax to return 3 to the shell as an
                        # error status
    jmp .exit           # Jump to the exit label

.exit:
    leave               # Function Epilogue
    ret                 # Function Epilogue
