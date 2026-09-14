const container = document.querySelector("[data-current-time-container]");
const time = document.querySelector("[data-current-time]");

if (container && time) {
  const formatter = new Intl.DateTimeFormat(
    document.documentElement.lang || undefined,
    {
      dateStyle: "medium",
      timeStyle: "short",
    },
  );

  const updateTime = () => {
    const now = new Date();

    time.dateTime = now.toISOString();
    time.textContent = formatter.format(now);
  };

  updateTime();
  container.hidden = false;
  window.setInterval(updateTime, 60_000);
}
