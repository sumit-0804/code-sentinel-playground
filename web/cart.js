export function total(items) {
  let sum = 0;
  for (const item of items) {
    sum += item.price * item.quantity;
  }
  return sum;
}

/**
 * Calculates the discounted total based on a promo code.
 * @param {number} total - The initial total amount.
 * @param {string} code - The discount code.
 * @returns {number} The total after applying the discount.
 */
export function discount(total, code) {
  const rate = code === "SAVE10" ? 0.1 : 0;
  const off = total * rate;
  return total - off;
}
