TODO
====

Add a watcher to the notification
-> check : - del
   	   - update
	   - create

we need to check in deep the tree of the directory Serie

-> modify the watcher for more efficiency

Notify
------

- Check if new series			     (1)
- Check if these series are able to download (2)
- Notify these series               	     (3)

(1) -> init : tab_series[] = 0
    -> end  : tab_series[] = all new episodes

(2) -> init : tab_series[] = all new episodes
    -> end  : tab_series[] = only episodes ready to download

(3) -> print tab_series (or send mail)

Bonus: when download, check if changement in directory tree then notify
