.STR1:  .string "Fibonacci(%d) = %d\n"
.STR2:  .string "Error: The integer must be greater than or equal to 0\n"
.STR3:  .string "Error: Please supply a single integer as an argument\n"

fib:
    push %rbp               # Function Prologue
    mov %rsp, %rbp          # Function Prologue
    mov %rdi, %r8           # Store the number in r8
    cmp $0,%r8              # Compare r8 to 0
    je .fib0                # If r8 == 0, jump to label .fib0
    cmp $1,%r8              # Compare r8 to 1
    je .fib1                # If r8 == 1, jump to label .fib1
    mov %r8, %r9            # Copy r8's value into r9, which will
                            # hold r8-1
    sub $1, %r9             # Subtract 1 from r9
    mov %r9, %rdi           # Move r9 into the first argument for fib()
    push %r8                # Save the value of r8
    call fib                # Call fib on r9
    pop %r8                 # Restore the value of r8
    mov %rax, %r9           # Store the return value of fib(r9) in r9
    mov %r8, %r10           # Copy r8's value into r10, which will
                            # hold r8-2
    sub $2, %r10            # Subtract 2 from r10
    mov %r10, %rdi          # Move r10 into the first argument for fib()
    push %r9                # Save the value of r9
    call fib                # Call fib on r10
    pop %r9                 # Restore the value of r9
    mov %rax, %r10          # Store the return value of fib(r10) in r10
    mov $0, %rax            # Move 0 into rax
    add %r9, %rax           # Add r9 to rax
    add %r10, %rax          # Add r10 to rax - rax now contains the
                            # value of r9 + r10, so we return it here
    leave                   # Function Epilogue
    ret                     # Function Epilogue

.fib0:                      # We get here if fib(0) is called and return 0
    mov $0, %rax            # Move 0 into rax
    leave                   # Function Epilogue
    ret                     # Function Epilogue

.fib1:                      # We get here if fib(1) is called and return 1
    mov $1, %rax            # Move 1 into rax
    leave                   # Function Epilogue
    ret                     # Function Epilogue

.globl main
main:
    push %rbp               # Function Prologue
    mov %rsp, %rbp          # Function Prologue
    cmp $2, %rdi            # Compare argc to 2
    jne .errargs            # If argc != 2, jump to the error message
                            # section
    mov %rsi, %r8           # Move argv into r8
    add $8, %r8             # Add 8 to r8 to get the pointer to argv[1]
    mov (%r8), %r8          # Dereference r8 and store the dereferenced
                            # value
                            # in r8
    mov %r8, %rdi           # Move r8 into rdi
    mov $0, %rax            # Move 0 into rax
    call atoi               # Call atoi on argv[1]
    mov %rax, %r8           # Move the return value from atoi into r8
    cmp $0, %r8             # Compare r8 to 0
    jl .errnum              # If the integer value in r8 is less than 0,
                            # exit the program
    mov %r8, %rdi           # Move r8 into the first argument for fib()
    push %r8                # Save the value of r8
    call fib                # Call fib()
    pop %r8                 # Restore the value of r8
    mov %rax, %r9           # Store fib()'s return value in r9
    mov %r9, %rdx           # Move fib()'s return value into third
                            # argument
                            # for printf()
    mov %r8, %rsi           # Move fib()'s argument into second argument for
                            # printf()
    mov $.STR1, %rdi        # Move the string into the first argument for
                            # printf()
    mov $0, %rax            # Move 0 into rax for printf()'s varargs
    call printf             # Call printf
    jmp .exit

.errnum:
    mov $.STR2, %rdi        # Move the error message into rdi
    mov $0, %rax            # Move 0 into rax
    call printf             # Print the error message
    jmp .exit               # Jump to the exit label

.errargs:
    mov $.STR3, %rdi        # Move the error message into rdi
    mov $0, %rax            # Move 0 into rax
    call printf             # Print the error message

.exit:
    mov $0, %rax            # Return 0
    leave                   # Function Epilogue
    ret                     # Function Epilogue
