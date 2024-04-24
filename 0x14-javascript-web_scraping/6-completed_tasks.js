#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const todos = JSON.parse(body);
  const taskCompleted = {};
  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      if (userId in taskCompleted) {
        taskCompleted[userId]++;
      } else {
        taskCompleted[userId] = 1;
      }
    }
  });
  console.log(taskCompleted);
});
