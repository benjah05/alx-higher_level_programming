#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let listLen = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    reversedList[i] = list[listLen];
    listLen--;
  }
  return reversedList;
};
