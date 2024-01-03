#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasksInfo = JSON.parse(body);

    const userCompletedTasks = {};

    tasksInfo.forEach(task => {
      if (task.completed) {
        if (!userCompletedTasks[task.userId]) {
          userCompletedTasks[task.userId] = 1;
        } else {
          userCompletedTasks[task.userId]++;
        }
      }
    });
    console.log(JSON.stringify(userCompletedTasks, null, 2).replace(/"(\d+)":/g, "'$1':"));
  }
});
