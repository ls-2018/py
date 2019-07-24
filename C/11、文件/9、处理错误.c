if (ferror(fp))
{
  /* display an error message */
  printf("Error reading from DUMMY.FIL\n");
  /* reset the error and EOF indicators */
  clearerr(fp);// 重置状态，归0
}
if (ferror (fp) == 0)  //
{
    printf ("正常\n");
}

else
{
    printf ("异常\n");
    perror("输出的错误是");//输出的错误是: Bad file descriptor
}