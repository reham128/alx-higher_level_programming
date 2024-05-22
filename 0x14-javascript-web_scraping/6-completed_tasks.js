#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const lists = JSON.parse(body);
  const userCompletedTasks = {};

  lists.forEach(list => {
    if (list.completed) {
      const userId = list.userId;
      userCompletedTasks[userId] = (userCompletedTasks[userId] || 0) + 1;
    }
  });
  console.log(userCompletedTasks);
});
