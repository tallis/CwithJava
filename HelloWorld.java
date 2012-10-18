/*
 *  #### C with JAVA using JNA ####
 * ### Author: Rui Costa ###
 *
 * # Sample Java File #
 * Java	code that calls a native library generated
 * by JNA with the C code.
 */
 
import com.sun.jna.Native;
import com.sun.jna.Library;
 
public class HelloWorld {
    public interface CExample extends Library {
        public void helloWorldfromC();
    }
    static public void main(String args[]) {
        CExample cCode = (CExample) Native.loadLibrary(args[0], CExample.class);
        cCode.helloWorldfromC();
    }
}
