const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from the Express Backend!');
});

app.listen(port, () => {
  console.log('Backend listening at http://0.0.0.0:${port}');
});
