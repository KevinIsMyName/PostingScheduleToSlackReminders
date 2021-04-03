function textToSchedule(text) {
  lines = text.split("\n");
  dates = {};
  for (let i = 2; i < lines.length; i++) {
    let day = lines[i].split(":")[0].trim();
    let posters = lines[i].split(":")[1].trim();
    dates[day] = posters;
  }
  schedule = {
    title: lines[0].split(":")[1].trim(),
    dates: dates,
  };
  return schedule;
}

function scheduleToBox(schedule, output) {
  // PARAMETER:
  let remindTime = "10am";

  let text = "";
  let title = schedule.title;
  for (const date in schedule.dates) {
    let names = schedule.dates[date];
    for (let i = 0; i < names.split(" ").length; i++) {
      let poster = names.split(" ")[i];
      text = text.concat(
        "/remind " +
          poster +
          ' "Please make a post about ' +
          String(title) +
          ' today. 11am-2pm are recommended." at ' +
          String(remindTime) +
          " " +
          String(date) +
          "\n"
      );

      console.log(text);
    }
  }
  output.value = text;
  console.log("Done writing to output.");
}
let output = document.getElementById("output");

document.getElementById("input").addEventListener("keyup", function () {
  let text = document.getElementById("input").value;
  let schedule = textToSchedule(text);
  console.log(schedule);
  scheduleToBox(schedule, output);
});

console.log("index.js loaded.");
