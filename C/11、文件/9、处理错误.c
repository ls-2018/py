if (ferror(fp))
{
  /* display an error message */
  printf("Error reading from DUMMY.FIL\n");
  /* reset the error and EOF indicators */
  clearerr(fp);// ����״̬����0
}
if (ferror (fp) == 0)  //
{
    printf ("����\n");
}

else
{
    printf ("�쳣\n");
    perror("����Ĵ�����");//����Ĵ�����: Bad file descriptor
}