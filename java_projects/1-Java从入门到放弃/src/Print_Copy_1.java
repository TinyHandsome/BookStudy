d main(String[] args) throws FileNotFoundException {

        PrintWriter pw = new PrintWriter(
                new BufferedOutputStream(
                        new FileOutputStream("print.txt")
                ), true
        );
  