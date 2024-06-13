// 권지민: dark/light 모드

document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.getElementById("themeToggle");
  const body = document.body;

  // Load the theme from localStorage
  const savedTheme = localStorage.getItem("theme") || "light";
  body.setAttribute("data-bs-theme", savedTheme);

  themeToggle.addEventListener("click", function () {
    const currentTheme = body.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    body.setAttribute("data-bs-theme", newTheme);

    // Save the theme to localStorage
    localStorage.setItem("theme", newTheme);
  });
});
