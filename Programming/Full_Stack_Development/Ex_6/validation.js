function validateForm() {
  let name = document.forms["regForm"]["name"].value;
  let email = document.forms["regForm"]["email"].value;
  let password = document.forms["regForm"]["password"].value;
  let mobile = document.forms["regForm"]["mobile"].value;

  if (name === "" || email === "" || password === "" || mobile === "") {
    alert("All fields must be filled!");
    return false;
  }

  let emailRegex = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!emailRegex.test(email)) {
    alert("Invalid email format!");
    return false;
  }

  if (password.length < 6) {
    alert("Password must be at least 6 characters!");
    return false;
  }

  let mobileRegex = /^[6-9]\d{9}$/;
  if (!mobileRegex.test(mobile)) {
    alert("Invalid mobile number!");
    return false;
  }

  alert("Registration successful!");
  return true;
}