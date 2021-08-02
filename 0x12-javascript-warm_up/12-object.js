#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const obj = myObject;
obj.value = 89;
console.log(myObject);
