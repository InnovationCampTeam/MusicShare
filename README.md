# 🎵 2024 SpartaCoding - NorthEast Innovation Camp

<aside>
  
**Duration:** 2024.06.12 09:00 ~ 2024.06.14 21:00

**Domain:** [Music Share](http://dlrjfdlfrdj.pythonanywhere.com)

This project is the result of a 3-day mini web project conducted during the Innovation Camp hosted by [Sparta Coding Club](https://spartacodingclub.kr). Three team members were responsible for implementing features and applying design. While it was challenging to include a wide range of features, the focus was on achieving stable and clear functionality.


## Introduction

- **Service Name:** Music Share
- **Description:** A web service for music lovers to create and share playlists.
- **Key Technologies:**
    - **FE:** HTML, CSS, JavaScript
    - **BE:** Python
    - **DB:** SQLite
    - **Library:** jQuery, Flask, Bootstrap
    - **Design:** Figma
    - **Collaboration Tools:** Git, GitHub, Notion
    - **Development Workflow:**
        - **main:** Manages the version deployed to users. Merges from develop branch.
        - **develop:** Collective development branch. Merges from feature branches.
        - **feature:** Branches created per issue. Automatically deleted after merge.
- **Project Duration:** 2024.06.12 ~ 2024.06.14

## 🌟 Crew

### Ryu Youngchan (류영찬)

[https://github.com/codingkunst](https://github.com/codingkunst)

### Kwon Jimin (권지민)

[https://github.com/mingzzi96](https://github.com/mingzzi96)

### Lee Seunghyeon (이승현)

[https://github.com/seunghyeonlee9661](https://github.com/seunghyeonlee9661)

## 🥇 Result

- **Brochure Submission**

    ![Brochure Image 1](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2024-06-14_150535.jpg)

    ![Brochure Image 2](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240616_100456.png)

    [Music Share](http://dlrjfdlfrdj.pythonanywhere.com/playlists/)

## 🔲 Wireframe

![Wireframe](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/Untitled%201.png)

## 📈 Features

<details>
  <summary>View Features</summary>

  - **Login Screen**
    
    ![Login Screen](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/Untitled%202.png)
    
    Enter user ID and password to login.
    
  - **Sign Up**
    
    ![Sign Up](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/Untitled%203.png)
    
  - **User Information Management**
    1. **Change Password:** Update password with new information.
        
        ![Change Password](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_134046.png)
        
    2. **Change Name:** Update user's name.
        
        ![Change Name](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_134328.png)
        
    3. **Delete Account:** Delete user account along with all playlists and music.
        
        ![Delete Account](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_134328_1.png)
        
  - **User Search and Friend Addition**
    1. **Search User:** Search other users by ID and add them as friends.
        
        ![Search User](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_102716.png)
        
    2. **Delete Friends:** Remove users from the friend list.
        
        ![Delete Friends](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/Untitled%204.png)
        
    3. **User Access Verification:** Only friends can access your playlists.
        
        ![Access Verification](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/Untitled%205.png)
        
    4. **Top Menu:** Allows user search by ID to share playlists easily. Added users can be removed by clicking the "x" button. Only friends can access other users' playlists.
  - **Playlist Creation/Deletion/Modification**

    ![Create Playlist](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_150535.jpg)
    
    Create a playlist with a name and image.

    ![Modify Playlist](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_150535_2.jpg)
    
    Modify the playlist name and image.

  - **Playlist Page**

    ![Playlist Page](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_150535_3.jpg)
    
    View your personal playlists.

  - **Add and Delete Music**

    Add and delete music from playlists.
    
    ![Add/Delete Music](2024%20NE%20Innovation%20Camp%20-%2014%20ac02e28f97144d15a099c4cedd3694ed/20240614_144832.png)

  - **Dark/Light Mode**

    Uses local storage to save the chosen color mode. This keeps the selected mode even after refreshing the page or reopening the site.

</details>

## ⚒️ Troubleshooting

- **Login Issues:**
    - Ensure that your username and password are correct.
    - If you have forgotten your password, use the password recovery feature.
    - Clear your browser’s cache and cookies, then try logging in again.
    - Check if the server is down for maintenance.

- **Playlist Errors:**
    - Verify that you have a stable internet connection.
    - Ensure that your playlist data is saved correctly.
    - Refresh the page or try logging out and logging back in.

- **Music Addition/Deletion Problems:**
    - Confirm that the music file format is supported.
    - Check if there is sufficient storage space.
    - Ensure that you have the necessary permissions to modify the playlist.

- **User Access Issues:**
    - Make sure that the user you are trying to share with is on your friend list.
    - Verify the user ID when searching for friends.
    - Refresh the page to see if the friend list updates.

## 🔗 Related Links

- **Documentation:**
    - [Project Documentation](http://dlrjfdlfrdj.pythonanywhere.com/docs)
    - [API Reference](http://dlrjfdlfrdj.pythonanywhere.com/api)
- **Project Management:**
    - [Notion Page](https://www.notion.so/InnovationCampTeam/MusicShare)
    - [GitHub Issues](https://github.com/InnovationCampTeam/MusicShare/issues)
