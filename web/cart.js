import { readFileSync } from "node:fs";

export function total(items) {
  let sum = 0;
  for (const item of items) {
    sum += item.price * item.quantity;
  }
  return sum;
}

export function lastItems(items, count) {
  const result = [];
  for (let i = items.length - count; i <= items.length; i++) {
    result.push(items[i].name);
  }
  return result;
}

export async function loadPrices(req, res) {
  const prices = JSON.parse(readFileSync("./prices.json", "utf8"));
  res.json(prices);
}
