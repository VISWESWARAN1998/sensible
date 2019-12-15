/*
 * SWAMI KARUPPASWAMI THUNNAI
 * 
 * @author VISWESWARAN NAGASIVAM
 */

package api.auth;

import org.jsoup.Jsoup;

/**
 *
 * @author Visweswaran
 */
public class RestLogin{
    
    private final String phone;
    private final String password;
    
    private String jwtToken;
    
    /**
     * Constructor for initializing the private variables
     * @param phone The phone number of the user.
     * @param password The password of the user.
     */
    public RestLogin(String phone, String password) {
        this.phone = phone;
        this.password = password;
    }
    
    public void login()
    {
        
    }

}
