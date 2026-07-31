const fs = require('fs');
function countStudents(path) {
  try {
    let data = fs.readFileSync
  } catch (err) {
    throw new Error('Cannot load the database')
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1);
  console.log(`Number of students: ${students.length}`);

  const fields = {};
  
}