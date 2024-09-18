/*Author: Stan Yin
* GitHub Name: SomeB1oody
* This project is based on CC 4.0 BY, please mention my name if you use it.
* This project requires opencv.
*/
#include<bits/stdc++.h>
#include<opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    cout << "Please enter image location" << endl;
    cout <<"Example: C:\\Wallpaper\\02.png" << endl;
    cout << "Enter HERE: ";
    string path;
    cin >> path;
    Mat img = imread(path, IMREAD_COLOR);
    if(img.empty())
    {
        cerr << "Error opening file" << endl;
        return -1;
    }
    int row_number = img.rows;
    int col_number = img.cols;

    if(row_number % 2 != 0) row_number -= 1;
    if(col_number % 2 != 0) col_number -= 1;

    int row_new = row_number / 2;
    int col_new = col_number / 2;

    Mat img_new = Mat::zeros(row_new, col_new, img.type());

    int symbol_row = 0, symbol_col = 0;

    for(int row = 0; row < row_new; row++)
    {
        for(int col = 0; col < col_new; col++) {
            symbol_row = row * 2;
            symbol_col = col * 2;
            Rect sector_rect(symbol_row, symbol_col, 2, 2);
            Mat sector = img(sector_rect);
            Scalar mean_color = mean(sector);
            Vec3b average_color;
            average_color[0] = static_cast<uchar>(mean_color[0]);
            average_color[1] = static_cast<uchar>(mean_color[1]);
            average_color[2] = static_cast<uchar>(mean_color[2]);
            img_new.at<Vec3b>(row, col) = average_color;
        }
    }
    namedWindow("Reduced Image");
    imshow("Reduced Image", img_new);
    waitKey(0);
    imwrite("Reduced_Image.jpg", img_new);
    return 0;
}
