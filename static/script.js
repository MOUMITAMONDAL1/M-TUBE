function showProgressBar() {
  const barContainer = document.getElementById('progressContainer');
  const progressBar = document.getElementById('progressBar');
  barContainer.classList.remove('hidden');

  let progress = 0;
  const interval = setInterval(() => {
    if (progress < 100) {
      progress += Math.random() * 10; // Fake animation
      progressBar.style.width = Math.min(progress, 100) + "%";
    } else {
      clearInterval(interval);
    }
  }, 300);
}
