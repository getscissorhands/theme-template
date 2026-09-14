document.querySelectorAll(".site-navigation").forEach((navigation) => {
  const entries = [...navigation.querySelectorAll(".navigation-toggle")].map(
    (button) => {
      const submenu = document.getElementById(
        button.getAttribute("aria-controls"),
      );
      const item = button.closest(".navigation-item");
      if (!submenu || !item || !item.contains(submenu)) {
        throw new Error("Navigation toggle must reference its own submenu.");
      }
      return { button, submenu, item };
    },
  );

  const close = (entry) => {
    for (const descendant of entries) {
      if (descendant === entry || entry.submenu.contains(descendant.button)) {
        descendant.button.setAttribute("aria-expanded", "false");
        descendant.submenu.hidden = true;
      }
    }
  };

  for (const entry of entries) {
    entry.button.addEventListener("click", () => {
      if (entry.button.getAttribute("aria-expanded") === "true") {
        close(entry);
        return;
      }
      for (const sibling of entries) {
        if (
          sibling !== entry &&
          sibling.item.parentElement === entry.item.parentElement
        ) {
          close(sibling);
        }
      }
      entry.submenu.hidden = false;
      entry.button.setAttribute("aria-expanded", "true");
    });
    entry.submenu.hidden = true;
    entry.button.hidden = false;
  }
  navigation.dataset.navigationEnhanced = "true";

  // Touch may move focus after pointerup; defer dismissal until the resulting click.
  let pointerDown = false;
  navigation.addEventListener("keydown", (event) => {
    pointerDown = false;
    if (event.key !== "Escape") return;
    const entry = entries.findLast(
      ({ button, item }) =>
        button.getAttribute("aria-expanded") === "true" &&
        item.contains(event.target),
    );
    if (entry) {
      event.preventDefault();
      event.stopPropagation();
      close(entry);
      entry.button.focus();
    }
  });

  document.addEventListener(
    "pointerdown",
    () => {
      pointerDown = true;
    },
    true,
  );
  document.addEventListener(
    "pointercancel",
    () => {
      pointerDown = false;
    },
    true,
  );

  navigation.addEventListener("focusout", (event) => {
    if (pointerDown) return;
    for (const entry of entries) {
      if (!entry.item.contains(event.relatedTarget)) close(entry);
    }
  });

  document.addEventListener("click", (event) => {
    pointerDown = false;
    if (!navigation.contains(event.target)) {
      for (const entry of entries) close(entry);
    }
  });
});

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
