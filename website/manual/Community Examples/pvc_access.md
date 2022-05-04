# Accessing PVC Data

### Where are my application files?
- Your files are held within the container
- They are not visible from your server's file structure without first mounting that PVC
<br />
<br />
<br />
<br />

# **Mounting PVC Data**
<br />
<br />


# Heavy_Script

One option is to use Heavy_Script.
If you plan on mounting PVC storage more than just a couple of times this may be the best option for you.
1. The script will list all of your PVC information for each application
2. Safely shut down your application before mounting
3. Mount your PVC to /mnt/temporary/STORAGE-NAME


The video will start at the mounting feature so you can see what it looks like.
Afterwards, if you wish to install it, follow the video guide starting at 15:52.

![type:video](https://youtu.be/uZp4x_Susgo?t=617)
<br />
<br />
<br />
<br />

# Manual Method - New User Guide 

Manually mounting PVC storage takes a little bit more time than the script method.
However, I know some users like to know exactly what commands they are running etc.

##### Recommended Items
- A terminal that allows copying and pasting
- An open notepad

1. **STOP the application you plan on mounting**
        
<br />

2. **Run the following command to view your PVC data**
    ```bash
    k3s kubectl get pvc -A | sort -u | awk '{print "\t" $1 "\t" $2 "\t" $4}' | column -t
    ```
        
<br />

3. **Next, find the application you would like to mount**
    - This can be confusing at first because many applications will have many different instances of PVC.
    - <a href="https://truecharts.org/_static/img/pvc_access/nextcloud_volumes.png"><img src="https://truecharts.org/_static/img/pvc_access/nextcloud_volumes.png" width="100%"/></a>
    - You'll see in this photo, Nextcloud has many different PVC's.
        - However, if you break it down by looking at the middle column, it's not too confusing.
        1. `data-nextcloud-redis-0 `
            - This is your Redis PVC
        2. `db-nextcloud-postgresql-0`
            - This is your PostgreSQL PVC
        3. `nextcloud-data`
            - This is your Data PVC
        
<br />

4. **After finding which PVC you would like to mount, copy the far right column (The Volume) that starts with pvc- into a notepad for use in the next command**
    - If I was wanting to mount `nextcloud-data`, I would use:
    - `pvc-cd84394b-7812-43c3-a6d9-1a5693592cbe`
        
<br />

5. **Run the following command to find the full path to your applications PVC**
    ```bash
    zfs list | grep PVC_VOLUME
    ```
    - Going off of the Nextcloud example, I would simply replace `PVC_VOLUME` with `pvc-cd84394b-7812-43c3-a6d9-1a5693592cbe`
    - Example: 
    ```bash
    zfs list | grep pvc-cd84394b-7812-43c3-a6d9-1a5693592cbe
    ```

    - Here is what the output should look like
        -   <a href="https://truecharts.org/_static/img/pvc_access/pvc_list.png"><img src="https://truecharts.org/_static/img/pvc_access/pvc_list.png" width="100%"/></a>

<br />

6.  **Mount your PVC**
    ```bash
    zfs set mountpoint=/temporary/NAME FULL_PVC_PATH
    ```
- Example: 
    ```bash
    zfs set mountpoint=/temporary/nextcloud-data speed/ix-applications/releases/nextcloud/volumes/pvc-cd84394b-7812-43c3-a6d9-1a5693592cbe
    ```
    - This command will produce no output if it's successful
    - Now you should be able to do whatever you want within the app's PVC
<br />
<br />   
<br />

### **Remounting**

```bash
zfs set mountpoint=legacy POOL_NAME/ix-applications/releases/APPLICATION_NAME/volumes/VOLUME-NAME
```
Example
```bash
zfs set mountpoint=legacy speed/ix-applications/releases/nextcloud/volumes/pvc-cd84394b-7812-43c3-a6d9-1a5693592cbe
```
        
<br />

Afterwards, I always like to ```rmdir``` on the directory that was created when mounting - In my case I would run:
```bash
rmdir /mnt/temporary/nextcloud-data
```
-   This just helps keep your temporary folder clean, and lets you know what is or is not currently mounted.
-   Do not worry, ```rmdir``` cannot delete mounted folders, or folders with contents in them.
<br />
<br />
<br />
<br />

# Manual Method - Advanced User Guide


#### **ALWAYS MAKE SURE THE APP IS STOPPED WHILE MOUNTING THE PVC**

#### To get the PVCNAME:
```bash
k3s kubectl get pvc -n ix-APPNAME
```
        
<br />

#### To get the PVCPATH:

```bash
zfs list | grep legacy | grep APPNAME
```
        
<br />

#### If you want to mount the PVC content:

```bash
zfs set mountpoint=/temporary PVCPATH
```

Your PVC will be mounted under `/mnt/temporary`

#### and when you're done editing:
        
<br />

```bash
zfs set mountpoint=legacy PVCPATH
```