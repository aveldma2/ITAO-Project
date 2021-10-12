# Feedback

## Overall
You did very good. Got through a lot of the actual functionality. You have tests for some of the more comnplicated things. Most of my feedback will be minor ways to improve your code.

Looks like you didn't quite get to figuring out how to work with getting a single object out of the db but you all still got pretty far.

## Files Structure

Be more consistent in naming things. A handful of suggestions
  - ORMPoll should not have ORM in the name. Not necessary. just call it Poll
  - Class names are capitalized but file names should be lower case. that is the convention among most programing languages
  - There are a lot of files in the models folder that shouldn't be there. A lot of "does this work" type files. Either put them in their own folder named appropriately for delete them. Remember you can go back and get them if you need to
  - another common thing to do is to have table names reflect the class names. So either `UserAnswer => user_answers` or 'Response => responses'

## Domain

Class names are singular (good) but you should have your file names be the same as well. Both in terms of the file name and the name being singular

I would probably keep the sessionmaker() add() and commit() commands out of classes. You can do all the prompting and setting variables inside the class but then doing the actual database transactions after that. In this case your classes know too much about the database process.

## Testing

Like that you do have a good number of tests

## CLI