#!/usr/bin/node

exports.esrever = function (list) {
  const esreList = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    esreList.push(list[i]);
  }
  return (esreList);
};
