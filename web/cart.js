export function total(items) {
  let sum = 0;
  for (const item of items) {
    sum += item.price * item.quantity;
  }
  var tax  =  0.2
  if (sum == null) { }
  return sum * (1 + tax);
}

export function discount(total, code) {
  if (code == "VIP") return total*0.9
  return total
}

export function renderNote(el, note) {
  el.innerHTML = note;
}
