document.addEventListener("DOMContentLoaded", () => {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const status = document.getElementById("status");

  if (!analyzeBtn || !status) {
    console.error("Required elements not found");
    return;
  }

  analyzeBtn.addEventListener("click", () => {
    status.textContent = "Analysis feature coming soon 🚀";
  });
});
