use std::fs;
use std::collections::HashMap;


fn main() {
    
    // Setup ans variable. 
    let mut ans = 0;

    // Define the file path
    let file_path = "/Users/ivancandelero/Desktop/AOC24/day1/input.txt";
    let trimmed_path = file_path.trim();

    // Read file 
    let contents = fs::read_to_string(trimmed_path)
        .expect("Failed to read the file");

    // Setup arrays left and right. 
    let mut left: [i32; 1000] = [0; 1000];
    let mut right: [i32; 1000] = [0; 1000];

    // Read the lines and fill in arrays
    for (i, line) in contents.lines().enumerate() {
        if i >= 1000 {
            // Prevent overflow if the file has more than 1000 lines
            break;
        }

        // Split the line into two numbers
        let numbers: Vec<&str> = line.split_whitespace().collect();

        // Filling up arrays with the values by the column.         
        if numbers.len() == 2 {
            // Parse the numbers and assign to the arrays
            left[i] = numbers[0].parse::<i32>().expect("Invalid number in left column");
            right[i] = numbers[1].parse::<i32>().expect("Invalid number in right column");
        }
    }

    
    // Sorting Arrays 
    left.sort();
    right.sort();

    // Calculating Part 1 answer
    for i in 0..left.len() {      
        // Finding the distance of the numbers. 
        ans += (left[i] - right[i]).abs();
    }

   
    // Use a HashMap to count occurrences of each number in the right list
    let mut right_counts = HashMap::new();
    for &num in &right {
        *right_counts.entry(num).or_insert(0) += 1;
    }

    // Calculate the similarity score for Part 2
    let mut similarity_score = 0;
    for &num in &left {
        if let Some(&count) = right_counts.get(&num) {
            similarity_score += num * count;
        }
    }

    // Answers 
    println!("Answer in Part 1: {}", ans);
    println!("Answer in Part 2 {}", similarity_score);

}
