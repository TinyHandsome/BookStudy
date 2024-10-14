export function increment (current, max = 10){
    if (current < max) {
        return current + 1;
    }
    return current
}

console.log(increment(1, 10))