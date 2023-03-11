document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'cs',
        firstDay: 1,
        displayEventTime: false,
        events: events
    });
    calendar.render();
});
var events =[
    {
        title: "Event 1",
        start: '2023-03-15T12:00:00',
        end: '2023-03-16T13:00:00',
        backgroundColor: 'red'
    },
    {
        title: "Event 2",
        start: '2023-03-12T00:00:00',
        end: '2023-03-16T01:00:00'
    }
]
