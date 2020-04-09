import Parse from 'parse';
export default function ({redirect}) {
    let currentUser = Parse.User.current();
    if(!currentUser)
        return redirect('/auth/login/');
  }
