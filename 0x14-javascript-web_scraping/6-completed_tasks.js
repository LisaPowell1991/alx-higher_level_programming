#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasksInfo = JSON.parse(body);

    const userCompletedTasks = {};

    tasksInfo.forEach((task) => {
      if (task.completed) {
        userCompletedTasks[task.userId] = (userCompletedTasks[task.userId] || 0) + 1;
      }
    });
    console.log('{', Object.entries(userCompletedTasks).map(([key, value]) => ` '${key}': ${value}`).join(',\n'), ' }');
  }
});
