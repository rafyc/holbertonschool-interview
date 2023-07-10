#!/usr/local/bin/node
import fetch from "node-fetch";
const args = process.argv;

const getChar = async () => {
  try {
    let res = await fetch(`https://swapi-api.hbtn.io/api/films/${args[2]}`)
    let data = await res.json()
    return data.characters;
  } catch (error) {
    console.log(error);
  }
}

const getName = async (url) => {
  try {
    let res = await fetch(url)
    let data = await res.json()
    console.log(data.name);
    return data.name;
  } catch (error) {
    console.log(error);
  }
}

const printNames = async () => {
  let arrName = await getChar();

  arrName.forEach(async (element) => {
    await getName(element);
  });
};

printNames();
