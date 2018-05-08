const request = require('request');
var slackBot = require('slack-bot')("https://hooks.slack.com/services/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");
const CronJob = require('cron').CronJob;
const argv = require('minimist')(process.argv.slice(2));

new CronJob('46 15 * * *', function() {
  (function checkCommits() {
    ['hassanmohaideen', 'Kimaitn', 'CristianPerez331', 'Areax', 'avikumar1'].forEach(function(ele) {
		request({
		  url: `https://api.github.com/users/${ele}/events`,
		  headers: {
			'User-Agent': 'keep-me-commiting'
		  }
		}, function (error, response, body) {
		  if (!error && response.statusCode == 200) {
			const lastEvent = JSON.parse(body)[0];
			if(!lastEvent)
			{
				slackBot.send({
				text: "You've never even committed to GitHub before @" + ele + "!",
				  channel: ['#github', `@${ele}`],
				  username: 'Commit_Reminder_Bot'
				});
				
			}
			else 
			{
				const now = new Date(Date.now()).toISOString();
				const lastEventTime = lastEvent.created_at;

				if (lastEvent.public) {
				  var daysSinceCommit = parseInt(now.split('-')[2].split('T')[0]) - parseInt(lastEventTime.split('-')[2].split('T')[0]);
				  if (daysSinceCommit > 14) {
					slackBot.send({
					text: "I've stopped keeping track, it's been at least two weeks.  @" + ele + ", run `git commit sudoku` in your terminal.",
					  channel: ['#github', `@${ele}`], // Can also be '@someone' for a direct message
					  username: 'Commit_Reminder_Bot'
					});
				  }
				  else if (daysSinceCommit > 7) {
					slackBot.send({
					text: "HEY! It's been " + daysSinceCommit + " days @" + ele + " since your last public commit. Get publicly shunned :(",
					  channel: ['#github', `@${ele}`], // Can also be '@someone' for a direct message
					  username: 'Commit_Reminder_Bot'
					});
				  }
				  else if (daysSinceCommit > 5) {
					slackBot.send({
					text: "We're getting to the " + daysSinceCommit + " day mark @" + ele + " since your last public commit. Do you need an ambulance?",
					  channel: ['#github', `@${ele}`], // Can also be '@someone' for a direct message
					  username: 'Commit_Reminder_Bot'
					});
				  }
				  else if (daysSinceCommit > 3) {
					slackBot.send({
					text: "You haven't made any public commits in the past @" + daysSinceCommit + " days " + ele + ". I'll check back tomorrow.",
					  channel: ['#github', `@${ele}`], // Can also be '@someone' for a direct message
					  username: 'Commit_Reminder_Bot'
					});
				  }
				}
			}
		  }
		});
	});
  })();
}, null, true, 'America/New_York');
