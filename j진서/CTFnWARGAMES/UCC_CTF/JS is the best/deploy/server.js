const fs = require('fs');
const express = require('express');

const port = 3000;
const flag = fs.readFileSync('flag.txt', 'utf8');

const app = express();
app.use(express.urlencoded({ extended: false }));


let stage = 0;
const q = [
  "('b'+'a'+ +'a'+'a').toLowerCase() == input",
  "typeof a == 'number' && a !== NaN && (a - 1 < a) == false",
  "Object.is(0, a) == false && Math.abs(1 / a) > 1",
  "input.length <= 6 && (eval(input) > 0) == false && (eval(input) == 0) == false && (eval(input) >= 0) == true",
  "input == 0 && input == 1",
];

app.get('/', (req, res) => {
  if (req.query.reset === 'true') {
    stage = 0;
  }
  res.send(`
    <h1>Stage: ${stage}</h1>
    <h2>${q[stage]}</h2>
    <form action="/check" method="post">
      ${stage == 1 || stage == 2 ? 'a = parseInt("<input type="text" name="input" />")' : 'input = "<input type="text" name="input" />"'}
      <input type="submit" value="Submit" />
    </form>
    <button onclick="window.location.href='/?reset=true'">Reset</button>
  `);
});

app.post('/check', (req, res) => {
  const input = req.body.input.toString() || '';
  let a;
  switch (stage) {
    case 0:
      if (input == ('b'+'a'+ +'a'+'a').toLowerCase()) {
        stage = 1;
      }
      break;
    case 1:
      a = parseInt(input);
      if (typeof a == 'number' && a !== NaN && (a - 1 < a) == false) {
        stage = 2;
      }
      break;
    case 2:
      a = parseInt(input);
      if (Object.is(0, a) == false && Math.abs(1 / a) > 1) {
        stage = 3;
      }
      break;
    case 3:
      if (input.length <= 6 && (eval(input) > 0) == false && (eval(input) == 0) == false && (eval(input) >= 0) == true) {
        stage = 4;
      }
      break;
    case 4:
      if (input == 0 && input == 1) {
        stage = 5;
        res.redirect('/flag');
      }
      break;
  }
  res.redirect('/');
});

app.get('/flag', (req, res) => {
  res.send(stage == 5 ? flag : 'Do not cheat!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});