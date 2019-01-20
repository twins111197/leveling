;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode
  (flycheck-checker . python-mypy)
  (eval . (setq default-directory (locate-dominating-file default-directory "mypy.ini")))))
