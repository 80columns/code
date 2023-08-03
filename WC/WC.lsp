(defun ProcessFile (FileName)
    "Process a file, counting its number of words + characters +
     lines"
    (setf c 0)
    (setf w 0)
    (setf rw 0)
    (setf l 0)
    (let ((in (open FileName :if-does-not-exist nil)))
      (when in
        ; Loop over the file for each character
        (loop for ch = (read-char in nil)
          ; Increment characters
          while ch do (incf c)
            (if
              ; If there is a newline, increment lines
              (char= ch #\newline)
              (incf l))
            ; If there is a word delimiter, and a word was being
            ; read, increment the words and unset the reading-word
            ; flag
            (if
              (and
                (or
                  (char= ch #\space)
                  (char= ch #\newline))
                (= rw 1))
              (progn (setf rw 0) (incf w))
              ; If there is a new word, set the reading-word flag
              (if
                (and
                  (char/= ch #\space)
                  (char/= ch #\newline)
                  (= rw 0))
                (setf rw 1))))
        (close in)))
    ; Print the file's output to stdout
    (format t "~D" l)
    (format t "~T")
    (format t "~D" w)
    (format t "~T")
    (format t "~D" c)
    (format t "~T")
    (format t FileName)
    (format t "~%"))

; Loop over the list of files in the argument list
(loop for Arg in *args* do (ProcessFile Arg))
