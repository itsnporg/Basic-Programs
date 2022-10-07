/**
Calculation of Value of PI using Bailey–Borwein–Plouffe Formula
**/

fn main() {
    // Buffer to read from stdin
    let mut input = String::new();

    println!("Enter the number of iterations: ");

    // Read the No of Terms of PI from stdin
    std::io::stdin().read_line(&mut input).unwrap();

    // Convert String to Integer
    let n = input.trim().parse::<u32>().unwrap();

    let mut pi = 0.0;

    for i in 0..n {
        let a1 = 4.0 / (8 * i + 1) as f64;
        let a2 = 2.0 / (8 * i + 4) as f64;
        let a3 = 1.0 / (8 * i + 5) as f64;
        let a4 = 1.0 / (8 * i + 6) as f64;

        pi += (a1 - a2 - a3 - a4) / ((16 as f64).powi(i as i32))
    }

    println!("Value of PI is {}", pi);
}

