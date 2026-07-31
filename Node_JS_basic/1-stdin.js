process.stdout.write("Welcome to Holberton School, what is your name?\n")
process.stdin.on("data", (inputname) => {
  process.stdout(`Your name is: ${inputname.toString().trim()\n}`);
});
process.stdin.on("end", () => {
  process.stdout.write("This important software is now closing\n");
});
