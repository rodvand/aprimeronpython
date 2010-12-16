      program precision_test
      real*8 a, b, c
      a = 1
      b = 10.0
      c = a/b
      write(*,*) 'Fortran program is running...'
      if (c .eq. 0.1) then
         write(*,*) 'c .eq. 0.1'
      end if
      if (c .eq. 1/10.0) then
         write(*,*) 'c .eq. 1/10.0'
      end if
      if (c .eq. a/b) then
         write(*,*) 'c .eq. a/b'
      end if
      end

