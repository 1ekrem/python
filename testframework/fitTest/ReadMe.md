# How to Structure a Simple Test
    Before you dive into writing tests, you’ll want to first make a couple of decisions:

**What do you want to test?**
Are you writing a unit test or an integration test?
Then the structure of a test should loosely follow this workflow:

**Create your inputs**
Execute the code being tested, capturing the output
Compare the output with an expected result
For this application, you’re testing sum(). There are many behaviors in sum() you could check, such as:

1. Can it sum a list of whole numbers (integers)?
1. Can it sum a tuple or set?
1. Can it sum a list of floats?
1. What happens when you provide it with a bad value, such as a single integer or a string?
1. What happens when one of the values is negative