export default function returnHowManyArguments(...args) {
  let count = 0;
  for (let i of args) {
    count += 1;
  }
  return count;
}
