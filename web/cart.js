export function total(items) {
  let sum = 0;
  for (const item of items) {
    sum += item.price * item.quantity;
  }
  return sum;
}

export function discount(total,code){
  const rate =  code==="SAVE10" ? 0.1 : 0
  const off = total*rate
  return total-off
}
